# Generated by Django 5.0.1 on 2024-02-18 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyPanel', '0006_rename_programename_subject_programe'),
        ('studentPanel', '0007_remove_student_program_name_student_program_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hallticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hallticketid', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facultyPanel.exam')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facultyPanel.program')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentPanel.student')),
            ],
        ),
    ]
