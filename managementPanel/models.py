from django.db import models
from userAuth.models import Person
from studentPanel.models import Student
from facultyPanel.models import Faculty


class Hod(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    userId = models.CharField(max_length=100, unique=True)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Event(models.Model):
    eventID=models.IntegerField()
    eventname=models.CharField(max_length=100)
    hod=models.ManyToManyField(Hod)
    description=models.TextField()
    starttime=models.DateField()
    duration=models.DurationField()

class Club(models.Model):
    clubid=models.IntegerField()
    clubname=models.CharField(max_length=100)
    hod=models.ManyToManyField(Hod)
    student=models.ManyToManyField(Student)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    estdate=models.DateField()
    type=models.CharField(max_length=100)
