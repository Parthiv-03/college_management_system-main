from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

import studentPanel.views
from . import views

# Create your views here.

def user_authantication(request):
    # authantication logic
    print("user_authantication")
    return render(request,'login.html')

