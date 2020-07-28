from django.shortcuts import render,redirect
from django.views import View
from .models import Activity
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required,permission_required
from .forms import ActivityForm
from datetime import datetime,date

class Index(LoginRequiredMixin,View):
    def get(self,request):
        template_name='activity/activity.html'
        activities = Activity.objects.filter(end_time__time__gt=datetime.now().time() ).order_by('-start_time')
        print(activities)
        InitialData={
            'end_time':'2020-07-09'
        }
        form=ActivityForm(initial=InitialData)
        context={
            'activities':activities,
            'form':form,
        }
        return render(request,template_name,context)

    def post(self,request): 
        permission_required = 'activity.add_activity'
        form=ActivityForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        messages.success(request,'activity created successfull!')
        return redirect('activity:index')




class Update(View):
    def post(self,request,*args,**kwargs):
            permission_required = 'activity.change_activity'
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

                
@login_required
@permission_required('activity.delete_activity')
def delete_activity(request,id):
    permission_required = 'activity.delete_activity'
    activity=Activity.objects.filter(id=id)[0]
    activity.delete()
    messages.success(request,'activity deleted successfull!')
    return redirect('activity:index')



def verify(request,id):
    activity=Activity.objects.filter(id=id)
    if (activity[0].status == False):
        activity.update(status=True)
        messages.success(request,f'Return of {activity[0].weapon} Verified successfull!')
        return redirect('activity:index')
    else:
       activity.update(status=False)
       messages.success(request,f'{activity[0].weapon} Return to Unverified state successfull!')
       return redirect('activity:index')


