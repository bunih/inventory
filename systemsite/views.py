from django.shortcuts import render,redirect
from django.views import View
from .models import SiteSystem
from .forms import SiteForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



class Index(LoginRequiredMixin,View):
    def get(self,request):
        sites=SiteSystem.objects.all()
        form=SiteForm()
        context={
            'sites':sites,
            'form':form
        }
        return render(request,'systemsite/systemsite.html',context)

    def post(self,request): 
        form=SiteForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        messages.success(request,'site created successfull!')
        return redirect('systemsite:index')




class Update(View):
    def post(self,request,*args,**kwargs):
            id_site=kwargs['id']
            site=SiteSystem.objects.filter(id=id_site)[0]
            form=SiteForm(request.POST or None,request.FILES or None,instance=site)
            if form.is_valid():
                form.save()
                messages.success(request,'site updated successfull!')
                return redirect('systemsite:index')
            else:
                print(form.errors)
                return redirect('systemsite:index')



def delete_systemsite(request,id):
    systemsite=SiteSystem.objects.filter(id=id)[0]
    systemsite.delete()
    messages.success(request,'site deleted successfull!')
    return redirect('systemsite:index')

