from django.shortcuts import render


def ChatRoom(req):
    return render(req,'chat.html')
