from django.apps import apps as django_apps
import re
from datetime import timedelta
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.utils.module_loading import import_string
from django.utils.crypto import constant_time_compare
from django.middleware.csrf import rotate_token
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from  rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, DjangoModelPermissions
from .permissions import IsOwner
from rest_framework.response import Response
from django.dispatch import receiver
from apps.authentication.serializers import UsersSerializer ,ProfileSerializer,UserLogoutSerializer, ResetTokenSerializer, CustomTokenObtainPairSerializer
from .models import  Users, Profile
from django.utils import timezone
from  django_rest_passwordreset.serializers import TokenSerializer, EmailSerializer, PasswordTokenSerializer
from django_rest_passwordreset.models import ResetPasswordToken, clear_expired, get_password_reset_token_expiry_time, get_password_reset_lookup_field
from django_rest_passwordreset.signals import reset_password_token_created, pre_password_reset, post_password_reset
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password, get_password_validators
from rest_framework import status, exceptions
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework_simplejwt.exceptions  import  InvalidToken, TokenError
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from django.core import serializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action

# Global  variables
HTTP_USER_AGENT_HEADER = getattr(settings, 'DJANGO_REST_PASSWORDRESET_HTTP_USER_AGENT_HEADER', 'HTTP_USER_AGENT')
HTTP_IP_ADDRESS_HEADER = getattr(settings, 'DJANGO_REST_PASSWORDRESET_IP_ADDRESS_HEADER', 'REMOTE_ADDR')

# Jwt view


# Signup View
# @swagger_auto_schema(operation_summary="Signup to  be used inside Admin side",query_serializer=UsersSerializer)
class SignupView(viewsets.ModelViewSet):
    """
     List, create, retrieve, update and destory user instances.
    """
    serializer_class = UsersSerializer
    permission_classes = (AllowAny, )
    http_method_names = ['post']

    def get_queryset(self):
        """
        Returns the object the view is displaying.
        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        if getattr(self, "swagger_fake_view", False):
            return User.objects.none()

        return User.objects.filter(id = self.request.auth.payload['id'])


## JWT  view recustomized as  GenericViewSet
class TokenViewBase(viewsets.GenericViewSet):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = None

    www_authenticate_realm = 'api'

    def get_authenticate_header(self, request):
        # add Exception for when login fails
        print('Authenticates Here')
        return f'{AUTH_HEADER_TYPES[0]} realm="{self.www_authenticate_realm}"'

    def create(self, request, format=None):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class TokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = CustomTokenObtainPairSerializer


class TokenRefreshView(TokenViewBase):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """
    serializer_class = jwt_serializers.TokenRefreshSerializer

# Logout View
class LogoutView(viewsets.GenericViewSet):
    """
    Logout the user
    """
    serializer_class = UserLogoutSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResetPasswordValidateToken(viewsets.GenericViewSet):
    """
    An Api View which provides a method to verify that a token is valid
    """
    throttle_classes = ()
    permission_classes = ()
    serializer_class = ResetTokenSerializer

    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_200_OK)


class ResetPasswordConfirm(viewsets.GenericViewSet):
    """
    An Api View which provides a method to reset a password based on a unique token
    """
    throttle_classes = ()
    permission_classes = ()
    serializer_class = PasswordTokenSerializer
    parser_classes = (JSONParser,)

    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data['password']
        token = serializer.validated_data['token']

        # find token
        reset_password_token = ResetPasswordToken.objects.filter(key=token).first()

        # change users password (if we got to this code it means that the user is_active)
        if reset_password_token.user.eligible_for_reset():
            pre_password_reset.send(sender=self.__class__, user=reset_password_token.user)
            try:
                # validate the password against existing validators
                validate_password(
                    password,
                    user=reset_password_token.user,
                    password_validators=get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
                )
            except ValidationError as e:
                # raise a validation error for the serializer
                raise exceptions.ValidationError({
                    'password': e.messages
                })

            reset_password_token.user.set_password(password)
            reset_password_token.user.save()
            post_password_reset.send(sender=self.__class__, user=reset_password_token.user)

        # Delete all password reset tokens for this user
        ResetPasswordToken.objects.filter(user=reset_password_token.user).delete()

        return Response(status=status.HTTP_200_OK)


class ResetPasswordRequestToken(viewsets.GenericViewSet):
    """
    An Api View which provides a method to request a password reset token based on an e-mail address
    Sends a signal reset_password_token_created when a reset token was created
    """
    throttle_classes = ()
    permission_classes = ()
    serializer_class = EmailSerializer
    parser_classes = (JSONParser,)

    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        # before we continue, delete all existing expired tokens
        password_reset_token_validation_time = get_password_reset_token_expiry_time()

        # datetime.now minus expiry hours
        now_minus_expiry_time = timezone.now() - timedelta(hours=password_reset_token_validation_time)

        # delete all tokens where created_at < now - 24 hours
        clear_expired(now_minus_expiry_time)

        # find a user by email address (case insensitive search)
        users = Users.objects.filter(**{'{}__iexact'.format(get_password_reset_lookup_field()): email})

        active_user_found = False

        # iterate over all users and check if there is any user that is active
        # also check whether the password can be changed (is useable), as there could be users that are not allowed
        # to change their password (e.g., LDAP user)
        for user in users:
            if user.eligible_for_reset():
                active_user_found = True

        # No active user found, raise a validation error
        # but not if DJANGO_REST_PASSWORDRESET_NO_INFORMATION_LEAKAGE == True
        if not active_user_found and not getattr(settings, 'DJANGO_REST_PASSWORDRESET_NO_INFORMATION_LEAKAGE', False):
            raise exceptions.ValidationError({
                'email': [(
                    "We couldn't find an account associated with that email. Please try a different e-mail address.")],
            })

        # last but not least: iterate over all users that are active and can change their password
        # and create a Reset Password Token and send a signal with the created token
        for user in users:
            if user.eligible_for_reset():
                # define the token as none for now
                token = None

                # check if the user already has a token
                if user.password_reset_tokens.all().count() > 0:
                    # yes, already has a token, re-use this token
                    token = user.password_reset_tokens.all()[0]
                else:
                    # no token exists, generate a new token
                    token = ResetPasswordToken.objects.create(
                        user=user,
                        user_agent=request.META.get(HTTP_USER_AGENT_HEADER, ''),
                        ip_address=request.META.get(HTTP_IP_ADDRESS_HEADER, ''),
                    )
                # send a signal that the password token was created
                # let whoever receives this signal handle sending the email for the password reset
                reset_password_token_created.send(sender=self.__class__, instance=self, reset_password_token=token)
        # done
        # token = serializers.serialize('json', [token.key, ])
        # print(token)
        return Response(status=status.HTTP_200_OK)

    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
        """
        Handles Password reset tokens
        When  a token is created ,  an email  needs to be sent to the user
        """
        # sends  an email  to the user
        try:
            # site_url = 'https://eprocure-backend.herokuapp.com/'
            site_url = 'http://localhost:8080/'
            context = ({
                'current_user': reset_password_token.user,
                'username': reset_password_token.user.username,
                'email': reset_password_token.user.email,
                'token': reset_password_token.key,
                'reset_password_url': f"{site_url}set-password/{reset_password_token.key}",
            })
            email_message = render_to_string('email/user_reset_password.html', context)
            email_subject = 'eProcure: Password Reset Email'
            email = EmailMultiAlternatives(subject=email_subject, body=email_message, to=[reset_password_token.user.email])
            email.attach_alternative(email_message, "text/html")
            email.send()
            print('password sent')
            return Response('status:ok',status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(f'error: {e}', status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailView(viewsets.ModelViewSet):
    """
    Profile Instances
    """
    #queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'pk'
    # permission_classes = (IsAuthenticated,)
    http_method_names = ['get','patch']

    def get_queryset(self):
        """
        This view should only  return the  current  user's profile
        """

        if getattr(self, "swagger_fake_view", False):
            return Profile.objects.none()

        user = self.request.user
        return Profile.objects.filter(user=user).select_related('user')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        print(f"This is the request{request.data}")
        return self.update(request, *args, **kwargs)

    @action(methods=['get'], detail=False, url_path='(?P<user_id>\d+)')
    def retrieve_profile(self, request, user_id,*args, **kwargs):
        profile = Profile.objects.get(user_id=user_id)

        if profile:
            serializer = self.get_serializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            context = {
                'detail': 'No profile found !'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
