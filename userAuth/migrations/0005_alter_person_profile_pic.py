# Generated by Django 5.0.1 on 2024-02-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0004_person_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
