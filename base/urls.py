from django.urls import path,include
from .views import *


app_name='base'
urlpatterns=[
    path('',Index.as_view() ,name='home'),
    path('user/',UserView.as_view() ,name='user'),
    path('activities/',ActivityView.as_view() ,name='activity'),
    path('norma-dashboard/',userDashboard ,name='user_dashboard'),
    path('<int:id>/',delete_activity,name='delete_activity' ),
]