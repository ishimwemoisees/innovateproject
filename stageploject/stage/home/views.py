from django.shortcuts import render

def home(request):
    homes = home.objects.all
    return render(request, 'home/home.html', {'homes': homes})
