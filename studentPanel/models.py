from django.db import models
from userAuth.models import Person
from facultyPanel.models import Program

class Student(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    roll_no = models.CharField(max_length=50,null=True)
    program=models.ForeignKey(Program,on_delete=models.CASCADE,null=True)
    degree = models.CharField(max_length=100,null=True)
    batch_year = models.IntegerField()
    admission_category = models.CharField(max_length=50,null=True)
    semester = models.IntegerField()