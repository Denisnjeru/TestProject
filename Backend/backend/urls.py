"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from rest_framework import routers, serializers, viewsets
from apps.authentication.urls import router as authentication_router
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# import apps.notification.urls
# Disable  the sidebar in  admin  portal
admin.autodiscover()
admin.site.enable_nav_sidebar = False


class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for extending url routes from another router.
    """

    def extend(self, router):
        self.registry.extend(router.registry)


router = DefaultRouter()
router.extend(authentication_router)


schema_view = get_schema_view(
   openapi.Info(
      title="Eprocure API",
      default_version='v1',
      description="Eprocure Backend API",
      terms_of_service="",
      contact=openapi.Contact(email="devops@qedsolutions.co.ke"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    # path('authentication/', include('authentication.urls')),
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('notifications/', include('apps.notification.urls'))
] + static(settings.MEDIA_DOWNLOAD_URL, document_root=settings.MEDIA_DOWNLOAD_ROOT)
