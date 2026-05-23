from django.db import models
from accounts.models import CustomUser
from restaurants.models import Restaurant
from tables.models import Table,TimeSlot

class Booking(models.Model):
    STATUS_CHOICES=(
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('cancelled','Cancelled'),
    )
    customer=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    table=models.ForeignKey(Table,on_delete=models.CASCADE)
    timeslot=models.ForeignKey(TimeSlot,on_delete=models.CASCADE)
    date=models.DateField()
    guests=models.IntegerField()
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username}-{self.restaurant.name}-{self.date}"
    
