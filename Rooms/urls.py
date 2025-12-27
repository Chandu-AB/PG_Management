from django.urls import path
from . import views
urlpatterns = [
    
   path("", views.rooms_dashboard, name="rooms_dashboard"),
   path('add/', views.add_room, name='add_room'),
   # path('list/', views.room_list, name='room_list'),
   path('room/<int:room_no>/', views.room_details, name='room_details'),

   
]