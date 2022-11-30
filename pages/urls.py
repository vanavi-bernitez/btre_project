from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name = 'index'), # '' empty means home page
    path('about', views.about, name = 'about'), # url.com/about 
]