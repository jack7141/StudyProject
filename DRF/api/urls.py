import os
from django.conf import settings
from django.urls import (path, include)
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from rest_framework import permissions
from .views import home

app_name = "api"
folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'versioned')
urlpatterns = []
version_map_dict = {}

for path, dirs, files, in os.walk(folder):
    # 목적: 폴더 하위(versioned)라는 폴더를 두고, v1, v2, v3로 버전을 관리하고 싶은건데ㅍ
    # C:\Users\ghl92\프로젝트\DRF\api\versioned ['v1'] ['__init__.py']
    print(path, dirs, files)
    # v1, v1\users, v2
    # 이런 방법 말고도 하위의 폴더들을 가지고 올 수 있는 방법이 있지 않을까? 
    # 좀 더 직관적인 방법
    print(path[len(folder) + len(os.path.sep):])
    depth = path[len(folder) + len(os.path.sep):].count(os.path.sep)
    # 0
    print(depth)
# urlpatterns = [
#     path('', home)
# ]

# for path, dirs, files, in os.walk(folder):
#     depth = path[len(folder) + len(os.path.sep):].count(os.path.sep)
#     if path != folder and depth == 1 and 'urls.py' in files:
#         version, api_name = path.split(os.path.sep)[-2:]
#
#         if not version_map_dict.get(version, None):
#             version_map_dict[version] = []
#
#         _include = 'api.versioned.{}.{}.urls'.format(version, api_name)
#
#         urlpatterns.append(url(r'^' + version + '/' + api_name + '/', include(_include)))
#         version_map_dict[version].append(url(r'^' + api_name + '/', include(_include), name=_include))


