
from django.urls import path

from blog.views import *

urlpatterns = [
    path('', list_post, name='list'),
    path('create/', create_post, name='create'),
    path('update/<int:pk>', update_post, name='update'),
    path('delete/<int:pk>', delete_post, name='delete'),
]
