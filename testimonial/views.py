from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def testimonial(request):
    


    dataTestimonial = Testimonial.objects.all()
    


    return render(request,  "crudProject/back/testimonial.html", { "dataTestimonial":dataTestimonial,} )



def newTestimonial(request):

    
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonial')
    else:
        form = TestimonialForm()

    return render(request,"crudProject/back/formPage.html", { "form": form, })


def destroyTestimonial(request, id):
    destroy = Testimonial(id)
    destroy.delete()
    
    return redirect('testimonial')


def update(request, id):
    

    edit = Testimonial.objects.get(id=1)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('testimonial')
    else:
        form = TestimonialForm(instance=edit)
    return render(request, 'crudProject/back/testimonial.html', {'form': form,})