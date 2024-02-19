from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def display_studentdashboard(request):
    return render(request, 'studentDashboard.html', {'title': 'home', 'sidebar': 'sidebars/studentSidebar.html'})
