from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ ModelViewSet 내부에 `create():post`, `retrieve(): get/{id}`, `update(): put`,
    `partial_update(): patch`, `destroy(): delete`  `list(): get

    """
    queryset = User.objects.all().order_by('-date_joined')
    """
    serializer_class : 입력된 값을 validate하거나 deserialize하거나, 
    출력값을 serialize할 때 사용하는 serializer 클래스. 
    일반적으로 이 속성을 설정하거나 get_serializer_class()메소드로 override해서 사용해야 함
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        pass

    def get_queryset(self):
        pass


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]