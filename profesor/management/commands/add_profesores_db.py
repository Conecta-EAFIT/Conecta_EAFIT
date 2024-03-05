# from django.core.management.base import BaseCommand
# from profesor.models import Profesor
# import os
# import json


# class Command(BaseCommand):
#     help= 'Load profesores from profesor_title.json en el modelo de profesor'

#     def handle(self, *args, **kwargs):
#         json_file_path = 'profesor/management/commands/profesores.json'

#         with open(json_file_path, 'r') as file:
#             profesores = json.load(file)

#         for i in range(10):
#             profesor = profesores[i]
#             exist = Profesor.objects.filter(title = profesor['title'].first())
#             if not exist:
#                 Profesor.objects.create(title = profesor['title'],
#                                         image = 'profesor/images/default.JPG',
#                                         genre = profesor['genre'],
#                                         year = profesor['year'])