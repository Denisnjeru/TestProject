from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authtokenviews
from . import views
from rest_framework_simplejwt import views as jwt_views
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm, reset_password_validate_token  
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

app_name = 'auth'

router = DefaultRouter()
router.register(r'auth/signup', views.SignupView, basename='signup')
# router.register(r'auth/login', views.LoginView, basename='login')
router.register(r'auth/logout', views.LogoutView, basename='logout')
# router.register(r'auth/profile', views.ProfileDetailView, basename= 'profile')
#router.register(r'auth/password_reset/', include('django_rest_passwordreset.urls'), 'password_reset')
router.register(r'auth/validate_token', views.ResetPasswordValidateToken, basename='reset-password-validate')
router.register(r'auth/confirm', views.ResetPasswordConfirm, basename='reset-password-confirm')
router.register(r'auth/reset_password_request', views.ResetPasswordRequestToken, basename='reset-password-request')
router.register(r'auth/token', views.TokenObtainPairView, basename='token_obtain_pair')
router.register(r'auth/token/refresh', views.TokenRefreshView, basename='token_refresh')

schema_view = get_schema_view(
   openapi.Info(
      title="Authentication API",
      default_version='v1',
      description="This  is the API for Authentication , where all the information about Authentication  is stored",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="njerudenis@qedsolutions.co.ke"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/',  schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', include(router.urls)),
    path('auth/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api-token-auth', authtokenviews.obtain_auth_token),
]
