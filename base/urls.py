from django.urls import path,include
from .views import *


app_name='base'
urlpatterns=[
    path('',Index.as_view() ,name='home'),
    path('norma-dashboard/',userDashboard ,name='user_dashboard'),
]