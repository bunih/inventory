from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Activity
from pprint import pprint

class Index(LoginRequiredMixin,View):
    def get(self,request):
        template_name='index.html'
        return render(request,template_name)
    
class ActivityView(LoginRequiredMixin,View):
    def get(self,request):
        template_name='activity/activity.html'
        activities = Activity.objects.order_by('-start_time')
        context={
            'activities':activities
        }
        return render(request,template_name,context)
    
class UserView(LoginRequiredMixin,View):
    def get(self,request):
        template_name='activity/activity.html'
        activities = Activity.objects.order_by('-start_time')
        context={
            'activities':activities
        }
        return render(request,template_name,context)
    

def userDashboard(request):
    template_name='activity/user_activity.html'
    user_activity = Activity.objects.filter(user=request.user)
    context={
            'activities':user_activity
        }
    return render(request,template_name,context)