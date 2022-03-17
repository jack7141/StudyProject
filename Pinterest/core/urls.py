from django.urls import path
# from cafes import views as CafeViews
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="CoreHomeView"),
]