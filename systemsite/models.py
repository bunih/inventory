from django.db import models

# Create your models here.


class SiteSystem(models.Model):
    name=models.CharField(max_length=100)
    guard=models.ForeignKey('User',on_delete=models.CASCADE)
    
    class Meta:
        db_table='sitesystem'


    def __str__(self):
        return self.name



