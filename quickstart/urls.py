from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^room/', views.TestView.as_view(), name='test-view'),
    url(r'^hostel/', views.HostelView.as_view(), name='hostel-view'),
]