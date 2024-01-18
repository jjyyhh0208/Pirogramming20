from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'devtools'

urlpatterns = [
    path('', tool_list, name='list'),
    path('create/', tool_create, name='create'),
    path('detail/<int:pk>', tool_detail, name='detail'),
    path('delete/<int:pk>', tool_delete, name='delete'),
    path('update/<int:pk>', tool_update, name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)