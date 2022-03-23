from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from accounts import models
from . import forms
from django.contrib.auth import authenticate, login, logout
import requests
import os
from django.core.files.base import ContentFile
from django.contrib import messages

class login_view(FormView):

    template_name = "accounts/login.html"
    form_class = forms.login_form
    # redirect reverse_lazy로 대체
    success_url = reverse_lazy("core:CoreHomeView")
    # initial = {
    #     "email":"ghl92479@gmail.com"
    # }

    # View로 구현한 if form.is_valid():를 아래 함수로 대체
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

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
    messages.info(request, f"See you later")
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
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        # User 인증 함수. 자격 증명이 유효한 경우 User 객체를, 그렇지 않은 경우 None을 반환
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        # user모델 이메일 함수 사용
        user.verify_email()
        return super().form_valid(form)

class profile_view(DetailView):

    model = models.User
    template_name = "accounts/user_detail.html"
    context_object_name = "target_user"


class profile_update_view(UpdateView):

    model = models.User
    template_name = "accounts/user_update.html"
    fields = (
        "first_name",
        "last_name",
        "avatar",
        "gender",
        "bio",
    )
    def get_object(self, queryset=None):
        return self.request.user

class profile_update_password_view(PasswordChangeView):
    template_name = "accounts/user_update_password.html"

def complete_verification(request, key):
    try:
        # 회원가입시 보내진 링크를 통해 접속했을 경우 실행!
        # 회원가입시 verify_email()이 통과한 후 저장된 email_secret과 일치하는 key가 있으면,
        # 이메일 검증 T로 바꾸고,
        # 검증되었으니, 이메일 시크릿키를 삭제한다.
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
    except models.User.DoesNotExist:
        # 에러 메세지 필요
        pass
    # 완료후 Home으로 다시 보내준다.
    return redirect("core:CoreHomeView")



class GoogleException(Exception):
    pass


def google_login(request):
    REST_API_KEY = os.environ.get("GOOGLE_KEY")
    REDIRECT_URI = "http://127.0.0.1:8000/accounts/login/google/callback"
    scope = "https://www.googleapis.com/auth/userinfo.email " + \
                "https://www.googleapis.com/auth/userinfo.profile"

    google_auth_api = "https://accounts.google.com/o/oauth2/v2/auth"
    response = redirect(
            f"{google_auth_api}?client_id={REST_API_KEY}&response_type=code&redirect_uri={REDIRECT_URI}&scope={scope}"
        )
        
    return response

def google_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("GOOGLE_KEY")
        client_secret = os.environ.get("GOOGLE_PASSWORD")
        redirect_uri = "http://127.0.0.1:8000/accounts/login/google/callback"
        state = "random_string"
        
        token_request = requests.post(
            f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={redirect_uri}&state={state}"
        )
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise GoogleException()
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://www.googleapis.com/oauth2/v3/userinfo",
            params={
                'access_token': access_token
            }
        )

        profile_json = profile_request.json()
        google_account = profile_json["email"]

        if google_account is None:
            raise GoogleException("Please also give me your email")
        nickname = profile_json["name"]
        profile_image = profile_json["picture"]
        try:
            user = models.User.objects.get(email=google_account)
            if user.login_method != models.User.LOGIN_GMAIL:
                raise GoogleException()
        except models.User.DoesNotExist:
            user = models.User.objects.create(
                email=google_account,
                username=google_account,
                first_name=nickname,
                login_method=models.User.LOGIN_GMAIL,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
            if profile_image is not None:
                photo_request = requests.get(profile_image)
                user.avatar.save(
                    f"{nickname}-avatar", ContentFile(photo_request.content)
                )
        login(request, user)
        messages.success(request, f"Welcome back {user.first_name}")
        return redirect("core:CoreHomeView")
    except GoogleException:
        messages.error(request, e)
        return redirect("accounts:login")    
    pass

class KakaoException(Exception):
    pass


def kakao_login(request):
    REST_API_KEY = os.environ.get("KAKAO_APP_KEY")
    REDIRECT_URI = "http://127.0.0.1:8000/accounts/login/kakao/callback"
    
    # 복사해올때 $ 없애는거 주의!
    return redirect(f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code')

def kakao_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("KAKAO_APP_KEY")
        redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback"
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
        )
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException()
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        kakao_account = profile_json.get("kakao_account", None)
        kakao_email = kakao_account['email']
        kakao_profile_data = kakao_account["profile"]
        if kakao_account['email'] is None:
            raise KakaoException("Please also give me your email")
        nickname = kakao_profile_data["nickname"]
        profile_image = kakao_profile_data["profile_image_url"]
        try:
            user = models.User.objects.get(email=kakao_email)
            if user.login_method != models.User.LOGING_KAKAO:
                raise KakaoException()
        except models.User.DoesNotExist:
            user = models.User.objects.create(
                email=kakao_email,
                username=kakao_email,
                first_name=nickname,
                login_method=models.User.LOGING_KAKAO,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
            if profile_image is not None:
                photo_request = requests.get(profile_image)
                user.avatar.save(
                    f"{nickname}-avatar", ContentFile(photo_request.content)
                )
        login(request, user)
        messages.success(request, f"Welcome back {user.first_name}")
        return redirect("core:CoreHomeView")
    except KakaoException as e:
        messages.error(request, e)
        return redirect("accounts:login")