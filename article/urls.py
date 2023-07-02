from django.contrib import admin
from django.urls import path

from . import views #bu uygulamanın içindeki views'ten al diyoruz.

app_name="article" #url'yi kullanırken verdiğimiz isim

urlpatterns = [
    path('dashboard/', views.dashboard,name="dashboard"),
    path('addarticle/', views.addarticle,name="addarticle"),
    path('article/<int:id>', views.detail,name="detail"),
    path('update/<int:id>', views.updateArticle,name="update"),
    path('delete/<int:id>', views.deleteArticle,name="delete"),
    path('', views.articles,name="article"),
    path('comment/<int:id>', views.addComment,name="comment"),

    
]