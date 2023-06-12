from django.shortcuts import render
from about.models import *
from skills.models import *
from portfolio.models import *
from services.models import *
from testimonial.models import *
from contact.models import *





# Create your views here.

def home(request):
    dataAbout= About.objects.all
    dataSkills= Skills.objects.all
    dataPortfolio= Portfolio.objects.all
    dataServices= Services.objects.all
    dataTestimonial= Testimonial.objects.all
    dataContact= Contact.objects.all

    return render (request, "crudProject/front/index.html", {"dataAbout": dataAbout, "dataSkills": dataSkills, "dataPortfolio": dataPortfolio, "dataServices": dataServices, "dataTestimonial": dataTestimonial, "dataContact": dataContact})



def alll(request):
    return render (request, "crudProject/back/all.html")

