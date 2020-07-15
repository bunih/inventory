from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class SiteSystem(models.Model):
    name=models.CharField(max_length=100)
    place=models.ForeignKey('Place',on_delete=models.CASCADE)
    start_time=models.DateTimeField(auto_now=True)
    end_time=models.DateTimeField()
    
    def  delete_systemsite(self):
        return reverse('systemsite:delete_systemsite',kwargs={'id':self.id})
    
    
    
    class Meta:
        db_table='sitesystem'

    def __str__(self):
        return self.name

class Place(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table='places'


