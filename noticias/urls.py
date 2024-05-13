from django.urls import path
from . import views
from conecta_django import urls
urlpatterns = [
    path('noticias/', views.noticias, name='noticias'),
    path('add_noticias/', views.add_noticias, name='add_noticias'),
    path('delete_noticias/<int:pk>', views.delete_noticias, name='delete_noticias'),
    path('update_noticias/<int:pk>', views.update_noticias, name='update_noticias')
]