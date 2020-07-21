from django.shortcuts import render,redirect
from django.views import View
from .models import Activity
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ActivityForm

class Index(LoginRequiredMixin,View):
    def get(self,request):
        template_name='activity/activity.html'
        activities = Activity.objects.order_by('-start_time')
        InitailData={
            'end_time':'2020-07-09'
        }
        form=ActivityForm(initial=InitailData)
        context={
            'activities':activities,
            'form':form,
        }
        return render(request,template_name,context)

    def post(self,request): 
        form=ActivityForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        messages.success(request,'activity created successfull!')
        return redirect('activity:index')




class Update(View):
    def post(self,request,*args,**kwargs):
            id_activity=kwargs['id']
            activity=Activity.objects.filter(id=id_activity)[0]
            form=ActivityForm(request.POST or None,request.FILES or None,instance=activity)
            if form.is_valid():
                form.save()
                messages.success(request,'activity updated successfull!')
                return redirect('activity:index')
            else:
                print(form.errors)
                return redirect('activity:index')

def delete_activity(request,id):
    activity=Activity.objects.filter(id=id)[0]
    activity.delete()
    messages.success(request,'activity deleted successfull!')
    return redirect('activity:index')


