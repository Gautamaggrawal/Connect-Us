from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'chat/signup.html', {})

@login_required
def room(request, room_name):
    return render(request, 'chat/chat.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username))
    })

@login_required
def roomname(request):
	return render(request, 'chat/roomname.html', {})



