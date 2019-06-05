# Generated by Django 2.2 on 2019-06-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_profesor_prostorija_termin_usertermin'),
    ]

    operations = [
        migrations.AddField(
            model_name='termin',
            name='casovi',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='termin',
            name='den',
            field=models.CharField(choices=[('PON', 'Понеделник'), ('VTO', 'Вторник'), ('SRE', 'Среда'), ('CET', 'Четврток'), ('PET', 'Петок')], default='PON', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='termin',
            name='vreme',
            field=models.IntegerField(choices=[(8, '8:00'), (9, '9:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'), (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00'), (19, '19:00')], default=8),
            preserve_default=False,
        ),
    ]
