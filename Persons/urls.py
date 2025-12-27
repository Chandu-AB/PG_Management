# Persons/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_person, name='add_person'),
    path('list/', views.person_list, name='person_list'),
   path("deactivate/<int:person_id>/", views.deactivate_person, name="deactivate_person"),
]
