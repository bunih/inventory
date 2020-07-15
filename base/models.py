from django.db import models
from django.conf import settings
from weapon.models import Weapon
from systemsite.models import SiteSystem
from django.urls import reverse
User=settings.AUTH_USER_MODEL

# Create your models here.
class Activity(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    weapon=models.ForeignKey(Weapon,on_delete=models.CASCADE)
    site=models.ForeignKey(SiteSystem,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    start_time=models.DateTimeField(auto_now=True)
    end_time=models.DateTimeField()

    def delete_activity(self):
        return reverse('base:delete_activity',kwargs={'id':self.id})


