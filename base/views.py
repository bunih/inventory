from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



class Index(LoginRequiredMixin,View):
    def get(self,request):
        template_name='index.html'
        return render(request,template_name)
    