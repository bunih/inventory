from django.shortcuts import render,redirect
from django.views import View
from .models import Weapon
from django.contrib import messages
from .forms import WeaponForm

class Index(View):
    def get(self,request):
        weapons=Weapon.objects.all()
        form=WeaponForm()
        context={
            'weapons':weapons,
            'form':form,
        }
        return render(request,'weapons/weapon_index.html',context)

    def post(self,request):
        print(request.POST)
        form=WeaponForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            print(form)
        messages.success(request,'weapon created successfull!')
        return redirect('weapons_index')




class Update(View):
    def post(self,request,*args,**kwargs):
            id_weapon=kwargs['id']
            weapon=Weapon.objects.filter(id=id_weapon)[0]
            form=WeaponForm(request.POST or None,request.FILES or None,instance=weapon)
            if form.is_valid():
                form.save()
            messages.success(request,'weapon updated successfull!')
            return redirect('weapons_index')

def delete_weapon(request,id):
    weapon=Weapon.objects.filter(id=id)[0]
    weapon.delete()
    messages.success(request,'weapon deleted successfull!')
    return redirect('../')