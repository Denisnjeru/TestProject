# import string
# import random
# from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType

from  .models import Users, Profile
from rest_framework import serializers, exceptions
from  rest_framework.serializers import ModelSerializer
from  rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from django.contrib.auth.models import User
import re
from django_rest_passwordreset.models import get_password_reset_token_expiry_time
from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404 as _get_object_or_404
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone
from  django_rest_passwordreset.models import ResetPasswordToken, ResetPasswordToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import update_last_login
from  .tokens import RefreshToken


class PasswordValidateMixin:
    def validate(self, data):
        token = data.get('token')

        # get token validation time
        password_reset_token_validation_time = get_password_reset_token_expiry_time()

        # find token
        try:
            reset_password_token = _get_object_or_404(ResetPasswordToken, key=token)
        except (TypeError, ValueError, ValidationError, Http404,
                ResetPasswordToken.DoesNotExist):
            raise Http404("The OTP password entered is not valid. Please check and try again.")

        # check expiry date
        expiry_date = reset_password_token.created_at + timedelta(
            hours=password_reset_token_validation_time)

        if timezone.now() > expiry_date:
            # delete expired token
            reset_password_token.delete()
            raise Http404("The token has expired")
        return data


class ResetTokenSerializer(PasswordValidateMixin, serializers.Serializer):
    token = serializers.CharField()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if settings.SIMPLE_JWT['UPDATE_LAST_LOGIN']:
            update_last_login(None, self.user)

        return data


class UserSerializer(ModelSerializer):
    """
    Get user details across the platform
    """
    class Meta:
        model = Users
        fields = ('id','username','first_name','last_name','email', 'user_type')
        read_only_fields = ('id','user_type')
        extra_kwargs = {
            'email': {'validators':[]}
        }


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'}
    )


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email'
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'read_only': True},
            'id': {'read_only': True},
        }
        validators = [
            UniqueTogetherValidator(
                queryset=Users.objects.all(),
                fields=('email',),
                message = 'A User with  email Already Exists'
            )
        ]


class UserLogoutSerializer(serializers.Serializer):
    username = serializers.CharField()



class ProfileSerializer(ModelSerializer):
    """
    Serializer the User Profile of the User
    """
    user = UserSerializer(many=False)
    permissions = serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()


    class Meta:
        model = Profile
        fields = ('user','profile_pic', 'phone_no', 'id_number', 'permissions', )



    def get_profile_pic(self, obj):
        request = self.context.get('request')
        if obj.profile_pic == '':
            return None
        photo_url = obj.profile_pic.url
        return request.build_absolute_uri(photo_url)

    def validate(self, data):
        """
        validate the phone number raises an error ifit dosent  match  the regex
        """
        reg = re.compile(r'^(?:\+?254)?[07]\d{8,9}$')

        if not reg.search(data['phone_no']):
            raise serializers.ValidationError(f"Invalid phone number please use the following formats +2547xxxxxxx,2547xxxxxxx,+25407xxxxxxx,25407xxxxxxx,07xxxxxxx")
        return data

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user.username = user_data.get('username', user.username)
        user.first_name = user_data.get('first_name', user.username)
        user.last_name = user_data.get('last_name', user.last_name)
        user.email = user_data.get('email', user.email)
        user.save()
        instance.user = user
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.id_number = validated_data.get('id_number', instance.id_number)
        instance.save()
        return instance
