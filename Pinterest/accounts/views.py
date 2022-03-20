from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import authenticate, login, logout

class login_view(FormView):

    template_name = "accounts/login.html"
    form_class = forms.login_form
    # redirect reverse_lazy로 대체
    success_url = reverse_lazy("core:CoreHomeView")
    initial = {
        "email":"ghl92479@gmail.com"
    }

    # View로 구현한 if form.is_valid():를 아래 함수로 대체
    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

# View로 구현
# class login_view(View):
#     """
#     로그인 기능 구현
#     """
#     def get(self, request):
#         form = forms.login_form()
#         return render(request, "accounts/login.html", {'forms':form})

#     def post(self, request):
#         # post 요청 처리
#         form = forms.login_form(request.POST)
#         # 입력값 유효성 검사
#         print(form.is_valid())
#         if form.is_valid():
#             # 유효성 통과 완료 후 email, password 가져오기
#             email = form.cleaned_data["email"]
#             password = form.cleaned_data["password"]

#             # User 인증 함수. 자격 증명이 유효한 경우 User 객체를, 그렇지 않은 경우 None을 반환
#             user = authenticate(request, username=email, password=password)
#             if user is not None:

#                 login(request, user)
#                 # Home으로 다시 돌려줌
#                 return redirect("core:CoreHomeView")
#         return render(request, "accounts/login.html", {'forms':form})
        

def log_out(request):
    logout(request)
    return redirect("core:CoreHomeView")

class sign_up_view(FormView):
    """
    로그인 기능 구현
    """
    template_name = "accounts/signup.html"
    form_class = forms.sign_up_form
    # redirect reverse_lazy로 대체
    success_url = reverse_lazy("core:CoreHomeView")
    initial = {
        "first_name" : "test",
        "last_name" : "test",
        "email" :"ghl92479@gmail.com"
    }

    def form_valid(self, form):
        """
        유효성 검사가 완료된 후 저장시키고 로그인까지 시킨다.
        """
        form.save()
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        # User 인증 함수. 자격 증명이 유효한 경우 User 객체를, 그렇지 않은 경우 None을 반환
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        # user모델 이메일 함수 사용
        user.verify_email()
        return super().form_valid(form)