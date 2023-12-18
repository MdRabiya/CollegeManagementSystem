# Generated by Django 4.2.7 on 2023-12-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0031_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('result_file', models.FileField(upload_to='result_files/')),
            ],
        ),
    ]