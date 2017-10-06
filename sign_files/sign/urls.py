"""
sign URL Configuration
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^sign/$', views.sign, name='sign'),
    url(r'^verify/$', views.verify, name='verify')
]
