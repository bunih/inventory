from django.shortcuts import render
from django.views import View
from .models import SiteSystem



class Index(View):
    def get(self,request):
        sites=SiteSystem.objects.all()
        context={
            'sites':sites
        }
        return render(request,'systemsite/systemsite.html',context)