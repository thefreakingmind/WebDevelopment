from django.shortcuts import render
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
