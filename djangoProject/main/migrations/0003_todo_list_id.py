# Generated by Django 2.1.5 on 2022-03-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220308_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='list_id',
            field=models.IntegerField(default=1),
        ),
    ]