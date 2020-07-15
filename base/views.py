from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Activity
from django.contrib import messages
from .forms import ActivityForm

class Index(LoginRequiredMixin,View):
    def get(self,request):
        template_name='index.html'
        return render(request,template_name)
    
class ActivityView(LoginRequiredMixin,View):
    def get(self,request):
        template_name='activity/activity.html'
        activities = Activity.objects.order_by('-start_time')
        form=ActivityForm()
        context={
            'activities':activities,
            'form':form,
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


def delete_activity(request,id):
    activity=Activity.objects.filter(id=id)[0]
    activity.delete()
    messages.success(request,'activity deleted successfull!')
    return redirect('base:activity')