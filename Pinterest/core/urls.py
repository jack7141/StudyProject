from django.urls import path
# from cafes import views as CafeViews
from arts.views import HomeView
from . import views

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="CoreHomeView"),
]