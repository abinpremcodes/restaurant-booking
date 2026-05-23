from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES=(
        ('customer','Customer'),
        ('restaurant_admin','Restaurant Admin'),
        ('super_admin','Super Admin'),
    )

    role=models.CharField(max_length=50,choices=ROLE_CHOICES,default='customer')
    phone=models.CharField(max_length=20,blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True,null=True)

    def is_customer(self):
        return self.role=='customer'
    
    def is_restaurant_admin(self):
        return self.role=='restaurant_admin'
    
    def is_super_admin(self):
        return self.role=='super_admin'
    


