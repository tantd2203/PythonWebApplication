from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class ShippingAddress (models.Model):

    full_name = models.CharField(max_length=300)

    email = models.CharField(max_length=250)

    address  = models.CharField (max_length=300)

    city =  models.CharField(max_length=250)

    #FK
    # Authenticated / not authenticated user (bear in mind)
    user = models.ForeignKey(User, on_delete=models.Case,null=True,blank=True)

    class Meta:
        
        verbose_name_plural = 'Shipping Address'

    
    def __str__(self) :
        
        return 'Shipping Address - ' +str(self.id)
