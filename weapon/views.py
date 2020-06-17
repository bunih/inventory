from django.shortcuts import render
from django.views import View
from .models import Weapon



class Index(View):
    def get(self,request):
        weapons=Weapon.objects.all()
        context={
            'weapons':weapons
        }
        return render(request,'weapons/weapon_index.html',context)