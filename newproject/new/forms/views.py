from django.shortcuts import render

from .models import Forms

from .forms import Formform, RawFormform


#def forms(request):
 #   form=RawFormform()
 #     form=RawFormform(request.POST)
   #   if form.is_valid():
   #       print(form.cleaned_data)
       #   Forms.objects.create(**form.cleaned_data)
     # else:
       #   print(form.errors)

   # context={
      #  'moise':form
  #  }
   # return render(request, 'forms/form.html', context)

#def forms(request):
   # print(request.GET)
    #print(request.POST)
    #context={ }
    #return render(request, 'forms/form.html', context)

def forms(request):
    form=Formform(request.POST or None)
    if form.is_valid():
        form.save()
        form=Formform()
    context={
        'moise':form

    }
    return render(request, 'forms/form.html', context)

def myform(request):
  obj=Forms.objects.all
  context={
      'x':obj
  }
  return render(request, 'forms/form.html', context)
