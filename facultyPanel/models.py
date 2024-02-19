from django.db import models
from userAuth.models import Person
# from studentPanel.models import Student


class Faculty(models.Model):

    person = models.OneToOneField(Person, to_field='user_id', on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name} - {self.designation}"

class Program(models.Model):
    program_name=models.CharField(max_length=100)
    departmentID=models.DecimalField(max_digits=10,decimal_places=2)
    program_duration=models.FloatField()

class Exam(models.Model):
    program=models.ForeignKey(Program,on_delete=models.CASCADE)
    examid=models.CharField(max_length=100)
    exam_type=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    duration=models.DurationField()
    program_name=models.CharField(max_length=100)
    totalmarks = models.DecimalField(max_digits=10,decimal_places=2)
    passingmark = models.DecimalField(max_digits=10,decimal_places=2)
    semester = models.DecimalField(max_digits=10,decimal_places=2)

class ExamPaper(models.Model):
    paperid=models.IntegerField(max_length=10)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)

class Subject(models.Model):
    subjectcode=models.CharField(max_length=20)
    subjectname=models.CharField(max_length=20)
    programe=models.ManyToManyField(Program)
    departmentid=models.IntegerField(max_length=10)
    refrencebook=models.CharField(max_length=20)

class Hallticket(models.Model):
    hallticketid=models.IntegerField()
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    student=models.ForeignKey('studentPanel.Student',on_delete=models.CASCADE)
    program=models.ForeignKey(Program,on_delete=models.CASCADE)


