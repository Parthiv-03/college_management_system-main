# Generated by Django 5.0.1 on 2024-02-09 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentPanel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demo',
            name='name',
        ),
    ]
