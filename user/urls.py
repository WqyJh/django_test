from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create_user),
    path('get', views.get_user),
    path('delete', views.delete_user),
]
