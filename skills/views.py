from django.shortcuts import render, redirect
from skills.models import *
from skills.forms import *


# Create your views here.
def skills(request):
    dataSkills= Skills.objects.all

    
    return render (request, "crudProject/back/skills.html",{"dataSkills":dataSkills})


def newSkills(request):

    dataSkills = Skills.objects.all()

    if request.method == 'POST':
        form = skillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = skillsForm()
    return render(request,"crudProject/back/skills.html", {"dataSkills" : dataSkills, 'form':form})


def destroySkills(request, id):
    destroy = Skills(id)
    destroy.delete()
    
    return redirect('skills')


def update(request, id):
    

    edit = Skills.objects.get(id=1)
    if request.method == 'POST':
        form = skillsForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = skillsForm(instance=edit)
    return render(request, 'crudProject/back/skills.html', {'form': form,})