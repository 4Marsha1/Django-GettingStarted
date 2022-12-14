from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Room, Message

# Create your views here.
def index(request): 
    return render(request, 'index.html')

def room(request, room): 
    username = request.GET["username"]
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {'room': room, 'username': username, 'room_details': room_details})

def checkView(request): 
    room = request.POST['room']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username) 

def send(request): 
    room_id = request.POST['room_id']
    username = request.POST['username']
    message = request.POST['message']
    print(room_id, username, message)
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    print(messages)
    return JsonResponse({'messages': list(messages.values())})