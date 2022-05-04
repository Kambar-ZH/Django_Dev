# Generated by Django 4.0.3 on 2022-05-04 21:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_course_created_alter_video_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 5, 4, 21, 29, 50, 668313, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='api.publisher'),
        ),
        migrations.AlterField(
            model_name='video',
            name='uploaded',
            field=models.DateField(default=datetime.datetime(2022, 5, 4, 21, 29, 50, 671957, tzinfo=utc)),
        ),
    ]