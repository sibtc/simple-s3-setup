from django.conf.urls import url
from django.contrib.auth import views as auth_views

from mysite.core import views


urlpatterns = [
    url(r'^$', views.DocumentCreateView.as_view(), name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^profile/$', views.PrivateDocumentCreateView.as_view(), name='profile'),
]
