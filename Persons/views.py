from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Person
from Rooms.models import Room
from collections import defaultdict

def add_person(request):
    if request.method == "POST":
        name = request.POST.get("name")
        parent_name = request.POST.get("parent_name")
        phone_no = request.POST.get("phone_no")
        adhar_raw = request.POST.get("adhar_no", "")
        # Keep only digits
        adhar_digits = ''.join(ch for ch in adhar_raw if ch.isdigit())
        # Validate length (Aadhaar should be 12 digits)
        if len(adhar_digits) != 12:
            messages.error(request, "Please enter a valid 12-digit Aadhaar number.")
            return redirect("add_person")
        # Format Aadhaar number with spaces after every 4 digits
        adhar_no = f"{adhar_digits[:4]} {adhar_digits[4:8]} {adhar_digits[8:12]}"
        address = request.POST.get("address")
        room_no = request.POST.get("room_no")
        start_date = request.POST.get("start_date")

        # Check duplicate Aadhaar
        if Person.objects.filter(adhar_no=adhar_no).exists():
            messages.error(request, "Aadhaar already exists!")
            return redirect("add_person")

        room = get_object_or_404(Room, room_no=room_no)
        active_count = Person.objects.filter(room_no=room, is_active=True).count()

        if active_count >= room.no_beds:
            messages.error(request, f"Room {room.room_no} is full!")
            return redirect("add_person")

        # Save person
        Person.objects.create(
            name=name,
            parent_name=parent_name,
            phone_no=phone_no,
            adhar_no=adhar_no,
            address=address,
            room_no=room,
            is_active=True,
            start_date=start_date
        )

        messages.success(request, f"{name} added successfully!")
        return redirect("person_list")

    # GET request
    rooms = Room.objects.all()
    room_data = []
    for room in rooms:
        active_count = Person.objects.filter(room_no=room, is_active=True).count()
        room_data.append({
            "room_no": room.room_no,
            "available_beds": room.no_beds - active_count
        })

    return render(request, "persons/add_person.html", {"rooms": room_data})


def update_room_availability(room):
    active_persons_per_room = Person.objects.filter(room_no=room, is_active=True).count()

    if active_persons_per_room >= room.no_beds:
        room.is_available = False
    else:
        room.is_available = True
    
    room.save()

def person_list(request):
    rooms = Room.objects.all().order_by('floor_no', 'room_no')

    room_persons = []

    for room in rooms:
        active_persons = room.person_set.filter(is_active=True).order_by('name')
        if active_persons.exists():
            room_persons.append({
                "room": room,
                "floor_no": room.floor_no,
                "data": {
                    "persons": active_persons,
                    "active_count": active_persons.count(),
                    "available_beds": room.no_beds - active_persons.count()
                }
            })

    return render(request, "persons/person_list.html", {"room_persons": room_persons})

def deactivate_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.is_active = False
    person.save()

    room = person.room_no
    update_room_availability(room)

    return redirect("person_list")


