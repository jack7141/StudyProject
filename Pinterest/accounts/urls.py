from django.urls import path
# from cafes import views as CafeViews
from . import views

app_name = "accounts"

urlpatterns = [
    path("login", views.login_view.as_view(), name="login"),
    path("login/kakao", views.kakao_login, name="kakao_login"),
    path("login/kakao/callback", views.kakao_callback, name="kakao_callback"),
    path("login/google", views.google_login, name="google_login"),
    path("login/google/callback", views.google_callback, name="google_callback"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.sign_up_view.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="complete_verification"),
]