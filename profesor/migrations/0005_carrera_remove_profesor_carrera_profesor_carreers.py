# Generated by Django 5.0.2 on 2024-04-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0004_merge_20240312_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_carreer', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='carrera',
        ),
        migrations.AddField(
            model_name='profesor',
            name='carreers',
            field=models.ManyToManyField(blank=True, related_name='profesores', to='profesor.carrera'),
        ),
    ]
