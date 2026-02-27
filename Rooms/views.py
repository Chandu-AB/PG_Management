from django.shortcuts import render, redirect,get_object_or_404
from .models import Room
from Persons.models import Person
from django.contrib.auth.decorators import login_required

@login_required
def add_room(request):
    if request.method == 'POST':
        room_no = request.POST.get('room_no')
        floor_no = request.POST.get('floor_no')
        no_beds = request.POST.get('no_beds')
        is_available = request.POST.get('is_available') == 'on'  # Checkbox

        # Save new room
        Room.objects.create(
            room_no=int(room_no),
            floor_no=int(floor_no),
            no_beds=int(no_beds),
            is_available=is_available
        )

        return redirect('room_list')  # Redirect to room list after save

    # GET request
    return render(request, 'rooms/add_room.html')


@login_required(login_url='login')
def rooms_dashboard(request):
    rooms = Room.objects.all().order_by("floor_no", "room_no")

    # Group rooms by floor (5 floors)
    floors = {}
    for room in rooms:
        floors.setdefault(room.floor_no, []).append(room)

    return render(request, "rooms/rooms_dashboard.html", {"floors": floors})

@login_required
def room_details(request, room_no):
    room = get_object_or_404(Room, room_no=room_no)

    # Get active persons
    persons = Person.objects.filter(room_no=room, is_active=True)
    occupied_beds = persons.count()
    available_beds = room.no_beds - occupied_beds
    is_full = room.is_full 
    return render(request, "rooms/room_details.html", {
        "room": room,
        "persons": persons,
        "occupied_beds": occupied_beds,
        "available_beds": available_beds,
        "is_full": is_full,
    })

