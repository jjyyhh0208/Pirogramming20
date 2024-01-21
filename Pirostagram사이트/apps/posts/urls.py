from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name='main'),
    path('create/', post_create, name='create'),
    path('detail/<int:pk>/', post_detail, name='detail'),
    path('delete/<int:pk>/', post_delete, name='delete'),
    path('update/<int:pk>/', post_update, name='update'),
]