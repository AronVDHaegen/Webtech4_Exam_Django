from django.urls import path

from . import views

urlpatterns = [
    path('', views.infractions, name='infractions'),
    path('<min>/', views.infractionsMin, name='infractionsMin'),
]