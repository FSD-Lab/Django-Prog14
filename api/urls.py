from django.urls import path
from .views import fetch_random_user, user_info, home

urlpatterns = [
    path("", home, name="home"),
    path("user-info/", user_info, name="user_info"),
    path("api/fetch_random_user/", fetch_random_user, name="fetch_random_user"),
]
