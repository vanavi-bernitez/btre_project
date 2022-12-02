from django.urls import path 

from . import views #from the current folder import the views

urlpatterns = [
    # path(1, 2, 3)
    # 1st param: route as a string. always end the route with < / >
    # 2nd param: passing reference to the function. Not calling it
    # 3rt param: name of the url 
    path('', views.index, name = 'index'), # '' empty means home page
    path('about', views.about, name = 'about'), # url.com/about 
]