from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from users.views import index_view

urlpatterns = [
    re_path(r'^$', auth_views.LoginView.as_view()),
    re_path(r'^index/$', index_view),
]
