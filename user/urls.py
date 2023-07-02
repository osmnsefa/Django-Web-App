from django.contrib import admin
from django.urls import path

from . import views #bu uygulamanın içindeki views'ten al diyoruz.

app_name="user" #url'yi kullanırken verdiğimiz isim

urlpatterns = [
    path('register/', views.register,name="register"),
    path('login/', views.loginUser,name="login"),
    path('logout/', views.logoutUser,name="logout"),
]