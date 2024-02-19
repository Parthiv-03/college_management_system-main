from django.db import models
from userAuth.models import Person
from studentPanel.models import Student


class Accountant(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    userId = models.CharField(max_length=100, unique=True)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()

class Payment(models.Model):
    accountant=models.ManyToManyField(Accountant)
    transID=models.CharField(max_length=100, unique=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    amount=models.IntegerField()
    payment_type = models.CharField(max_length=100)
    chequeNo=models.IntegerField()
    time=models.TimeField()
    semester=models.IntegerField()
    