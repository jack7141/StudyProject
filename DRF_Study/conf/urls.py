"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import (path, include)
from rest_framework import routers
from api import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# URL의 끝에 붙이는 슬래시(/)를 트레일링 슬래시(trailing slash)라고 부릅니다
"""
https://www.google.com/example/ -> 디렉토리입니다.
https://www.google.com/example -> 파일입니다.
"""
router = routers.DefaultRouter(trailing_slash=False)
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('reviews', views.ReviewViewSet)

# FIXME: 왜 라우터로는 안되지?
# router.register('status', views.StatusViewSet.as_view({'get': 'status'}), basename="status")


# router.register('', views.UserViewSet)
# swagger 연결
schema_view = get_schema_view(
    openapi.Info(
        title='Question API',
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # patterns=schema_url_patterns,
)



urlpatterns = [
    path('', include(router.urls)),
    path('status/', views.StatusViewSet.as_view({'get': 'status'})),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('api/', include('api.urls'))
]
