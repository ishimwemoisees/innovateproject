from django.shortcuts import render
from .models import Service
def service(request):
    a=Service.objects.all
    context={
        'data':a # a and data are varibles
    }

    return render(request, 'service/service.html', context)

