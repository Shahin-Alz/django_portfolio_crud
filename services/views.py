
from django.shortcuts import render, redirect
from services.models import *
from services.forms import *


# Create your views here.
def services(request):

    return render (request,"crudProject/back/services.html")



def newService(request):

    dataServices = Services.objects.all()

    if request.method == 'POST':
        form = servicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = servicesForm()
    return render(request,"crudProject/back/services.html", {"dataServices" : dataServices, 'form':form})


def destroySkills(request, id):
    destroy = Services(id)
    destroy.delete()
    
    return redirect('services')


def update(request, id):
    

    edit = Services.objects.get(id=1)
    if request.method == 'POST':
        form = servicesForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = servicesForm(instance=edit)
    return render(request, 'crudProject/back/skills.html', {'form': form,})