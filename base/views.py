from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from activity.models import Activity

class Index(LoginRequiredMixin,View):
    def get(self,request):
        template_name='index.html'
        return render(request,template_name)
        
class NormalDashboard(LoginRequiredMixin,View):
    def get(self,request):
        template_name='normal_dashboard.html'
        user_activities = Activity.objects.order_by('-start_time')
        user_activities = Activity.objects.filter(user=self.request.user).order_by('-start_time')
        context={
            'activities':user_activities,
        }
        return render(request,template_name,context)

    