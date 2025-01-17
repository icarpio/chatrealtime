from django.shortcuts import render,  get_object_or_404
from .models import ChatRoom


def index(request):
     rooms = ChatRoom.objects.all()
     return render(request, 'chat/index.html', {
        'username': request.user.username,
        'rooms': rooms  # Pasa el username al template
    })


def room(request, room_name):
    chat_room = get_object_or_404(ChatRoom, identifier=room_name)
    return render(request, 'chat/room.html', {
        'room_name_json': chat_room.identifier,  # Sigue siendo útil para WebSockets
        'room_name': chat_room.name,  # Pasamos el nombre de la sala al template
        'username': request.user.username
    })
