"""
sign_files URL Configuration
"""

from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('sign.urls'))
]
