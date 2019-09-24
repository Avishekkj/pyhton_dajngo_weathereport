from django.contrib import admin
from django.urls import path
from . import views

app_name ='bookrepo'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'<int:book_id>/',views.details,name='details'),

]