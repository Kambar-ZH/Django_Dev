# Generated by Django 4.0.3 on 2022-04-28 18:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='publisher',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='api.publisher'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 4, 28, 18, 35, 20, 134798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='video',
            name='uploaded',
            field=models.DateField(default=datetime.datetime(2022, 4, 28, 18, 35, 20, 137226, tzinfo=utc)),
        ),
    ]
