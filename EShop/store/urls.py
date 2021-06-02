
from django.contrib import admin
from django.urls import path
from .views import signup, login, home
urlpatterns = [
    path('', home.index, name = "indexpage"),
    path('signup', signup.Signup.as_view(), name = "signup"),
    path('login', login.Login.as_view(), name = "login")
]
