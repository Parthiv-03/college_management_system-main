# Generated by Django 5.0.1 on 2024-02-18 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acPanel', '0002_accountant_userid'),
        ('studentPanel', '0007_remove_student_program_name_student_program_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transID', models.CharField(max_length=100, unique=True)),
                ('amount', models.IntegerField()),
                ('payment_type', models.CharField(max_length=100)),
                ('chequeNo', models.IntegerField()),
                ('time', models.TimeField()),
                ('semester', models.IntegerField()),
                ('accountant', models.ManyToManyField(to='acPanel.accountant')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentPanel.student')),
            ],
        ),
    ]
