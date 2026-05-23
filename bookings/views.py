from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from restaurants.models import Restaurant
from tables.models import Table,TimeSlot

@login_required
def booking_create(request,restaurant_id):
    restaurant=get_object_or_404(Restaurant,pk=restaurant_id)
    timeslots=TimeSlot.objects.filter(restaurant=restaurant)

    if request.method=='POST':
        date=request.POST['date']
        timeslot_id=request.POST['timeslot']
        guests=request.POST['guests']

        timeslot=get_object_or_404(TimeSlot,pk=timeslot_id)
        table=Table.objects.filter(
        restaurant=restaurant,
        capacity__gte=guests).first()

        if table:

           Booking.objects.create(
            customer=request.user,
            restaurant=restaurant,
            table=table,
            timeslot=timeslot,
            date=date,
            guests=guests,
                           )
           return redirect('booking_list')
        else:
            error='No tables are availabale for your group size!'
            return render (request,'bookings/booking_create.html',{
            'restaurant':restaurant,
            'timeslots':timeslots,
            'error':error,
        })
    return render(request,'bookings/booking_create.html',{
        'restaurant':restaurant,
        'timeslots':timeslots,
        
    })

@login_required
def booking_list(request):
    bookings=Booking.objects.filter(customer=request.user)
    return render (request,'bookings/booking_list.html',{'bookings':bookings})

@login_required
def booking_cancel(request,pk):
    booking=get_object_or_404(Booking,pk=pk)
    if request.method=='POST':
        booking.status='cancelled'
        booking.save()
        return redirect('booking_list')
    return render (request,'bookings/booking_cancel.html',{'booking':booking})



    

    

