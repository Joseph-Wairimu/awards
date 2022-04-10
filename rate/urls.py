from django.urls import path,register_converter,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rate/profile/', views.profile, name='profile'),
    path('rate/edit_profile/', views.edit_profile, name='edit_profile'),
    path('rate/search_results/', views.search_results, name='search_results'),
    path('rate/project_post/',views.create_project,name='new-post'),
    path('register/', views.register, name='register'),
    path('',include('django.contrib.auth.urls')),
    path('rate_project/<id>/',views.rate_project,name='rate_project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
   