from django.db import models
from accounts .models import CustomUser

class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    cuisine=models.CharField(max_length=50)
    location=models.CharField(max_length=500)
    image=models.ImageField(upload_to='restaurants/',blank=True,null=True)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    is_approved=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
