from django.db import models
from restaurants.models import Restaurant

class Table(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    table_number=models.CharField(max_length=10)
    capacity=models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} - {self.restaurant.name}"
    
class TimeSlot(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    time=models.TimeField()

    def __str__(self):
        return f"{self.time} - {self.restaurant.name}"
    
    



    

