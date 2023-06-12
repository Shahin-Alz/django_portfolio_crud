from django.shortcuts import render, redirect
from .models import *
from .forms import * 

# Create your views here.


def about(request):

    dataAbout= About.objects.all

    return render (request, "crudProject/back/about.html", {"dataAbout": dataAbout})


def updateAbout(request):
    

    edit = About.objects.get(id=1)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AboutForm(instance=edit)
    return render(request, 'crudProject/back/about.html', {'form': form,})