# Generated by Django 2.2 on 2019-06-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190602_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='poraka',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]