from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from restaurants.models import Restaurant

@login_required
def add_review(request,restaurant_id):
    restaurant=get_object_or_404(Restaurant,pk=restaurant_id)
    if request.method=='POST':
        rating=request.POST['rating']
        comment=request.POST['comment']
        Review.objects.create(
            customer=request.user,
            restaurant=restaurant,
            rating=rating,
            comment=comment,   
        )
        return redirect ('restaurant_detail',pk=restaurant_id)
    return render (request,'reviews/add_review.html',{'restaurant':restaurant})

def review_list(request,restaurant_id):
    restaurant=get_object_or_404(Restaurant,pk=restaurant_id)
    reviews=Review.objects.filter(restaurant=restaurant)
    return render(request,'reviews/review_list.html',
                  {'restaurant':restaurant,
                   'reviews':reviews})















        


