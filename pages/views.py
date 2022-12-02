from django.shortcuts import render
from django.http import HttpResponse

"""
def name(took a request):
    returns a response 
    i.e. pull data from db
         send email 
"""

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')