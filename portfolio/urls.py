from django.urls import path
from django.conf.urls import handler404, handler500 

from . import views

app_name='portfolio'

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
]
