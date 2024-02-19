from django.contrib.auth.models import User
from django.db import models
# from PIL import Image

class Person(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default.jpg')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    house_no = models.CharField(max_length=20, blank=True)
    street_name = models.CharField(max_length=100, blank=True)
    area_landmark = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    pincode = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    religion = models.CharField(max_length=50, blank=True)
    program_name = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    batch_year = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True)
    mother_tongue = models.CharField(max_length=50, blank=True)
    blood_group = models.CharField(max_length=5, blank=True)
    mother_name = models.CharField(max_length=50, blank=True)
    father_name = models.CharField(max_length=50, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    mobile_no = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    roll_number = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=100, blank=True)
