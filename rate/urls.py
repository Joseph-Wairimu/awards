from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('rate/profile/', views.profile, name='profile'),
    path('rate/edit_profile/', views.edit_profile, name='edit_profile'),
    path('rate/search_results/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
   