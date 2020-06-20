from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from .views import *


app_name='systemsite'
urlpatterns = [
    path('',Index.as_view(),name='site_index' ),
   

]