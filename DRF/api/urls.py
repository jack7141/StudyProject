import os
from django.conf import settings
from django.urls import (path, include)
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from rest_framework import permissions
from .views import home as home_view

app_name = "api"
folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'versioned')
urlpatterns = []
version_map_dict = {}


urlpatterns = [
    path('', home_view)
]

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


