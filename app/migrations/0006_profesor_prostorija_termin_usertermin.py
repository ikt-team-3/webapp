# Generated by Django 2.2 on 2019-06-05 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190604_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=100)),
                ('prezime', models.CharField(max_length=100)),
                ('titula', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'profesori',
            },
        ),
        migrations.CreateModel(
            name='Prostorija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'prostorii',
            },
        ),
        migrations.CreateModel(
            name='UserTermin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korisnik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termini', to='app.Korisnik')),
                ('predmet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Predmet')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profesor')),
                ('prostorija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Prostorija')),
            ],
        ),
        migrations.CreateModel(
            name='Termin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predmet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termini', to='app.Predmet')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termini', to='app.Profesor')),
                ('prostorija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termini', to='app.Prostorija')),
            ],
            options={
                'verbose_name_plural': 'termini',
            },
        ),
    ]
