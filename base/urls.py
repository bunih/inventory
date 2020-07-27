from django.urls import path,include
from .views import *


app_name='base'
urlpatterns=[
    path('',NormalDashboard.as_view() ,name='home'),
    path('',Index.as_view() ,name='normal_dashboard'),
]