"""
URL configuration for conecta_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from profesor import views as profesorViews
from ingreso import views as ingresoViews
from noticias import views as noticiasViews
from usuario import views as usuarioViews

from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ingresoViews.home1, name='home1'),
    path('home1', ingresoViews.home1, name='home1'),
    path('login/', ingresoViews.login, name='login'),
    path('signup/', ingresoViews.signup, name='signup'),
    path('signout/', ingresoViews.signout, name='signout'),
    path('about/', profesorViews._about, name='about'),
    path('record/<int:pk>', profesorViews.customer_record, name='record'),
    path('profesores/', profesorViews._profesores, name='profesores'),
    path('Conecta/', profesorViews.conectaHome, name='conectaHome'),
    path('noticias/', noticiasViews.noticias, name='noticias' ),     
    path('add_record/', profesorViews.add_record, name='add_record' ),
    path('delete_record/<int:pk>', profesorViews.delete_record, name='delete_record'),
    path('profesor_por_carrera/<str:carrera_id>/', profesorViews.profesor_por_carrera, name='profesor_por_carrera'),
    path('update_record/<int:pk>', profesorViews.update_record, name='update_record') ,
    path('conectaHome_admin/', usuarioViews.custom_login, name='conectaHome_admin'),
    path('<str:nombreP>/<int:pk>', profesorViews.plantillaProfesor, name='plantillaProfesor'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
