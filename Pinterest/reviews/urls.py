from django.urls import path
# from cafes import views as CafeViews
from . import views

app_name = "reviews"

urlpatterns = [
    # path("create", views.review_create_view.as_view(), name="ReviewCreate"),
    path("create/<int:id>", views.review_create_view, name="ReviewCreate"),
]