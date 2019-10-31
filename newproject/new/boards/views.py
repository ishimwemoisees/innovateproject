from django.shortcuts import render
from .models import Board

def nome(request):
    boards = Board.objects.all()
    return render(request, 'boards/nome.html', {'boards':boards})
