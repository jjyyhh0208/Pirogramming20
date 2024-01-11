from django.urls import path
from .views import *

urlpatterns = [
    path('', reviews_list),
    path('<int:pk>', reviews_read),
    path('create', reviews_create),
    path('delete/<int:pk>', reviews_delete),
    path('update/<int:pk>', reviews_update),
]