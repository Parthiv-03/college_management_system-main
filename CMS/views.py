from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . import views


# Create your views here.
def display_indexpage(request):
    return render(request, 'index.html',{'title':'welcome', 'sidebar':'sidebars/blank.html'})

def r(request):
    return HttpResponse("hello world")