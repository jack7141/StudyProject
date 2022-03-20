from django.urls import path
# from cafes import views as CafeViews
from arts.views import HomeView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="CoreHomeView"),
]