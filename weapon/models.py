from django.db import models

# Create your models here.


class Weapon(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    image=models.ImageField()

    class Meta:
        db_table='weapons'
        pass


    def __str__(self):
        return self.name



