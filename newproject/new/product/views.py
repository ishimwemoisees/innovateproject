from django.shortcuts import render

from .models import Product

from .forms import Productform
def product(request):
    form = Productform(request.POST or None)
    if form.is_valid():
        form.save()
        form=Productform()
    context = {
       'papa':form
    }
    return render(request, 'product/product.html', context)


def myform(request):
    obj = Product.objects.all
    context = {
        'p':obj
    }
    return render(request, 'product/product.html', context)

