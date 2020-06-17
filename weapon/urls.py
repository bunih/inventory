from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from .views import *



urlpatterns = [
    path('',Index.as_view(),name='weapons_index' ),
   

]