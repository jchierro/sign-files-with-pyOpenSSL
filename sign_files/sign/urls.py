"""
sign URL Configuration
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^sign/$', views.SignView.as_view(), name='sign'),
    url(r'^verify/$', views.VerifyView.as_view(), name='verify')
]
