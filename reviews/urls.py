from django.urls import path
from .import views
urlpatterns=[
    path('<int:restaurant_id>/add/',views.add_review,name='add_review'),
    path('<int:restaurant_id>/',views.review_list,name='review_list'),

]