from django.urls import path
# from cafes import views as CafeViews
from . import views

app_name = "accounts"

urlpatterns = [
    path("login", views.login_view.as_view(), name="login"),
]