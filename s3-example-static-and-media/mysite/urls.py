from django.conf.urls import url
from django.contrib.auth import views as auth_views

from mysite.core import views


urlpatterns = [
    url(r'^$', views.DocumentCreateView.as_view(), name='home'),
]
