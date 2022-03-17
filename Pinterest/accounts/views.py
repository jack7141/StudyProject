from django.shortcuts import render
from django.views import View

class login_view(View):
    """
    로그인 기능 구현
    """
    def get(self, request):
        return render(request, "accounts/login.html")

    def post(self, request):
        pass