# Generated by Django 5.0.2 on 2024-03-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='genre',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
