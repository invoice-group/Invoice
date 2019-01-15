from django.urls import path, include, re_path

from web import views
urlpatterns = [
    path('index/', views.index),
    path('test/', views.test),
]
