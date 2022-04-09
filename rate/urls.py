from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rate/profile/', views.profile, name='profile'),
    path('rate/edit_profile/', views.edit_profile, name='edit_profile'),
]
   