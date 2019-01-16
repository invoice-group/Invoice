from django.urls import path, include, re_path

from web import views
urlpatterns = [
    path('test/', views.test),
]
