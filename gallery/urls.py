from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('photo/<str:slug>', PhotoDetail.as_view(), name='detail'),
    path('add-photo', CreateCard.as_view(), name='create_photo')
]