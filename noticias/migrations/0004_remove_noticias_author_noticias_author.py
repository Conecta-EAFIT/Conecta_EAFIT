# Generated by Django 5.0.2 on 2024-05-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_remove_noticias_author_noticias_author'),
        ('profesor', '0009_profesor_education_alter_profesor_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='author',
        ),
        migrations.AddField(
            model_name='noticias',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='noticias', to='profesor.profesor'),
        ),
    ]
