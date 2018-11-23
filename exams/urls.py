__author__ = 'Pareng Jay'
from django.urls import path

from . import views

urlpatterns=[
    path('',views.index, name='home'),
    path('auth/', views.auth, name='auth'),
]
