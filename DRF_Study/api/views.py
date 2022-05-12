from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    from django_filters import rest_framework as filters
    # GenericViewSet의 역할이 중요
    """ ModelViewSet method 정리
    `list(): get',
    `create():post`,
    `retrieve(): get/{id}`,
    `update(): put`,
    `partial_update(): patch`,
    `destroy(): delete`
    - 근데 여기서 내가 원하는 부분만 남기고 지우고 싶으면 어떻게 처리해야하지?
    1)
    : ModelViewSet 에는 이미 메소드들이 정해져있기 때문에, 내가 필요한 mixins클래스를 상속받아서
    사용한다 아래가 예시다.

    from rest_framework import viewsets, mixins
    class SampleViewSet(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    위와 같이 처리하면, 수정과 삭제의 기능만 갖게된다.

    2)
    내가 사용하고 싶은 메소드만 골라서 쓸수 있게해줌
    http_method_names = ['get', 'post', 'patch']

    # get 부분이 action이라고 칭한다.
    path(r'dump', AccountDumpViewSet.as_view({'get': 'dump'})),
    """
    queryset = User.objects.all().order_by('-date_joined')
    """
    serializer_class : 입력된 값을 validate하거나 deserialize하거나, 
    출력값을 serialize할 때 사용하는 serializer 클래스. 
    일반적으로 이 속성을 설정하거나 get_serializer_class()메소드로 override해서 사용해야 함
    """

    serializer_class = UserSerializer
    # def get_serializer_class(self):
    #     return UserSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields를 사용하면, swagger상에서 던지는 파라미터를 내가 원하는걸로 수정할 수 있다.
    # /user?email=tset@asdf.com&username=asdifjaslf
    # https://www.django-rest-framework.org/api-guide/filtering/ -> Django Filter
    filter_fields = ('email', 'username',)
    permission_classes = [permissions.IsAuthenticated]

    # def filter_queryset(self, queryset):
    #     queryset = queryset.filter(**self.kwargs)
    #     queryset = super().filter_queryset(queryset=queryset)
    #     return queryset


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()

    # serializer_class를 사용하여 설정하거나, get_serializer_class()를 사용하여 처리
    # serializer_class = GroupSerializer
    def get_serializer_class(self):
        return GroupSerializer
    permission_classes = [permissions.IsAuthenticated]