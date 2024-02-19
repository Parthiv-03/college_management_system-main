from django.shortcuts import render

from studentPanel.models import Student
from userAuth.models import Person
from django.contrib.auth.models import User


def x(request):
    # u = User.objects.create_user(username='abc', password='<PASSWORD>')
    # a = Student.objects.create_user(qualification='xxx')
    # p.save()
    # print(p)
    return render(request, 'updateAttendance.html',{'title':'Add Marks','sidebar':'sidebars/facultySidebar.html'})