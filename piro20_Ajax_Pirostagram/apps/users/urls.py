from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'users'

urlpatterns = [
    path('', main, name='main'),
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('update/', user_update, name='update'),
    path('detail/', user_detail, name='detail'),
    path('delete/', user_delete, name='delete'),
]