from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create ),
    path('list_all', views.list_all)
]