from django.urls import path
from c1 import views

urlpatterns = [
    path('about', views.index, name='index'),
]
