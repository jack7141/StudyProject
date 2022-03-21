import imp
from django.contrib.auth.models import User
from .models import Art
from django.http import HttpResponseForbidden


def art_ownership_required(func):
    def decorated(request, *args, **kwargs):
        art = Art.objects.get(pk=kwargs['pk']) # db에서 가져온 user
        print(request.id, art)
        if not art.artist == request.user: # 우항은 클라이언트가 입력한 user값
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated