from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib.auth import authenticate, login, logout
class login_view(View):
    """
    로그인 기능 구현
    """
    def get(self, request):
        form = forms.login_form()
        return render(request, "accounts/login.html", {'forms':form})

    def post(self, request):
        # post 요청 처리
        form = forms.login_form(request.POST)
        # 입력값 유효성 검사
        print(form.is_valid())
        if form.is_valid():
            # 유효성 통과 완료 후 email, password 가져오기
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # User 인증 함수. 자격 증명이 유효한 경우 User 객체를, 그렇지 않은 경우 None을 반환
            user = authenticate(request, username=email, password=password)
            if user is not None:

                login(request, user)
                # Home으로 다시 돌려줌
                return redirect("core:CoreHomeView")
        return render(request, "accounts/login.html", {'forms':form})
        

def log_out(request):
    logout(request)
    return redirect("core:CoreHomeView")

class sign_up_view(View):
    """
    로그인 기능 구현
    """
    def get(self, request):
        pass

    def post(self, request):
        pass