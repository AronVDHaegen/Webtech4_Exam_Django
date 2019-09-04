from django.urls import path

from . import views

urlpatterns = [
    path('', views.infractions, name='infractions'),
]