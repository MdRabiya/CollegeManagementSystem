# Generated by Django 4.2.7 on 2023-12-04 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0036_course_student_alter_studentform_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
    ]
