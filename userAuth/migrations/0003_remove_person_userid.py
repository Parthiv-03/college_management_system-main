# Generated by Django 5.0.1 on 2024-02-17 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0002_remove_person_aadhar_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='userId',
        ),
    ]