from django.shortcuts import render,redirect
from django.views import View
from .models import SiteSystem
from django.contrib import messages



class Index(View):
    def get(self,request):
        sites=SiteSystem.objects.all()
        context={
            'sites':sites
        }
        return render(request,'systemsite/systemsite.html',context)


def delete_systemsite(request,id):
    systemsite=SiteSystem.objects.filter(id=id)[0]
    systemsite.delete()
    messages.success(request,'site deleted successfull!')
    return redirect('../')