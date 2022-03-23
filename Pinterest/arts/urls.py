from django.urls import path
# from cafes import views as CafeViews
from . import views

app_name = "arts"

urlpatterns = [
    path("create", views.ArtCreateView.as_view(), name="viewCreate"),
    path("detail/<int:id>", views.ArtDetailView.as_view(), name="viewDetail"),
    path("update/<int:id>", views.ArtUpdateView.as_view(), name="viewUpdate"),
    path("delete/<int:id>", views.ArtDeleteView.as_view(), name="viewDelete"),
    path("list/<int:pk>", views.ArtshotosView.as_view(), name="viewArtist"),
    path('likes/<int:id>', views.likes, name='likes'),
]