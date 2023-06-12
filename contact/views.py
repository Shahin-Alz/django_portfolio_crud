from django.shortcuts import render, redirect
from contact.models import *
from contact.forms import *

# Create your views here.
def contact(request):
    dataContact= Contact.objects.all
    return render(request, "crudProject/back/contact.html", {"dataContact": dataContact})
        


def updateContact(request):
    

    edit = Contact.objects.get(id=1)
    if request.method == 'POST':
        form = contactForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = contactForm(instance=edit)
    return render(request, 'crudProject/back/contact.html', {'form': form,})