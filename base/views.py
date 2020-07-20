from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class Index(LoginRequiredMixin,View):
    def get(self,request):
        template_name='index.html'
        return render(request,template_name)
    

def userDashboard(request):
    template_name='activity/user_activity.html'
    user_activity = Activity.objects.filter(user=request.user)
    context={
            'activities':user_activity
        }
    return render(request,template_name,context)


