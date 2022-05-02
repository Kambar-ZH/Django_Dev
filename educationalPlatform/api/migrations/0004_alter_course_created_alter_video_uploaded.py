# Generated by Django 4.0.3 on 2022-04-28 19:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_course_created_alter_course_publisher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 4, 28, 19, 45, 12, 779361, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='video',
            name='uploaded',
            field=models.DateField(default=datetime.datetime(2022, 4, 28, 19, 45, 12, 783595, tzinfo=utc)),
        ),
    ]
