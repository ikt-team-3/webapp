# Generated by Django 2.2 on 2019-06-05 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190605_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertermin',
            name='prostorija',
        ),
    ]
