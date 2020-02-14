from django.shortcuts import render



def index(request):
    return render(request, 'websocketapp/index.html', {})

def room(request, room_name):
    return render(request, 'websocketapp/room.html', {
        'room_name': room_name
    })