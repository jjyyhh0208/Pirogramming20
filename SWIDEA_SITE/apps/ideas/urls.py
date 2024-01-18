from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ideas'

urlpatterns = [
    path('', main, name='main'),
    path('detail/<int:pk>', detail, name='detail'),
    path('create/', create, name='create'),
    path('delete/<int:pk>', delete, name='delete'),
    path('update/<int:pk>', update, name='update'),
    path('increase/<int:id>/', increase_interest, name='increase-interest'),
    path('decrease/<int:id>/', decrease_interest, name='decrease-interest'),
    path('arrange/', my_list_view, name='arrange')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)