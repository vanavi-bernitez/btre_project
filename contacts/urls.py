from django.urls import path
from . import views

urlpatterns = [
    # path(1, 2, 3)
    # 1st param: route as a string. always end the route with < / >
    # 2nd param: passing reference to the function. Not calling it
    # 3rt param: name of the url 
    path('contact', views.contact, name = 'contact')
]