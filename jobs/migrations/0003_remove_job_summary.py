# Generated by Django 2.0.1 on 2018-05-18 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20180518_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='summary',
        ),
    ]
