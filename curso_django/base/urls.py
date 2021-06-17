from django.urls import path

from curso_django.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
