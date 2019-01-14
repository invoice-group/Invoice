from django.urls import path, include, re_path
from web.views import hello
from web.views import login
from web.views import SaveProfile
from web.views import index
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# app_name = 'hello'
urlpatterns = [
    path('hello/', hello),
    path('connection/', TemplateView.as_view(template_name = 'login.html')),
    path('login/', login, name = 'login'),
    path('profile/', TemplateView.as_view(template_name = 'profile.html')),
    path('saved/', SaveProfile),
    path('index/', index),
]

urlpatterns += staticfiles_urlpatterns()