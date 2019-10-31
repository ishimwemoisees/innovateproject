from django.shortcuts import render
from .models import Video

def video(request):
    x=Video.objects.all
    context={
        'y':x
    }
    return render(request, 'video/video.html', context)
