from django.shortcuts import render, get_object_or_404
from .models import Products
from .forms import UserForm
from django.http import HttpResponse
def index(request):
    obj = Products.objects.all()
    context = {
            "object":obj
        }
    return render(request, 'Products/index.html', context)

def upload(request):
    form = UserForm()
    if request.method=='POST':
        form = UserForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            return HttpResponse("Thanks for Submitting")

    return render(request, 'Products/upload.html', {'form':form})


def detailed_view(request, pk):
    obj = get_object_or_404(Products, pk=pk)
    context = {
            "object":obj
            }
    return render(request, 'Products/detail.html', context)


