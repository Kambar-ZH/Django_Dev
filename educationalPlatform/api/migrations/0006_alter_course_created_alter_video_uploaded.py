# Generated by Django 4.0.3 on 2022-05-04 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_course_created_alter_course_publisher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='video',
            name='uploaded',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
