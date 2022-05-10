from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ ModelViewSet method 정리
    `list(): get',
    `create():post`,
    `retrieve(): get/{id}`,
    `update(): put`,
    `partial_update(): patch`,
    `destroy(): delete`
    - 근데 여기서 내가 원하는 부분만 남기고 지우고 싶으면 어떻게 처리해야하지?
    """
    queryset = User.objects.all().order_by('-date_joined')
    """
    serializer_class : 입력된 값을 validate하거나 deserialize하거나, 
    출력값을 serialize할 때 사용하는 serializer 클래스. 
    일반적으로 이 속성을 설정하거나 get_serializer_class()메소드로 override해서 사용해야 함
    """
    # serializer_class를 사용하여 설정하거나, get_serializer_class()를 사용하여 처리
    # serializer_class = UserSerializer
    def get_serializer_class(self):
        return UserSerializer

    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    # serializer_class = GroupSerializer
    def get_serializer_class(self):
        return GroupSerializer
    permission_classes = [permissions.IsAuthenticated]