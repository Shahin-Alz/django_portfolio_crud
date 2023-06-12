from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def portfolio(request):
    


    dataFilter = Filter.objects.all()
    dataPortfolio = Portfolio.objects.all()


    return render(request,  "crudProject/back/portfolio.html", {"dataPortfolio": dataPortfolio, "dataFilter":dataFilter,} )



def newImage(request):

    
    if request.method == 'POST':
        form = portfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = portfolioForm()

    return render(request,"crudProject/back/formPage.html", { "form": form, })

def newFilter(request):

    
    if request.method == 'POST':
        form1 = filterForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('portfolio')
    else:
        form1 = filterForm()

    return render(request,"crudProject/back/formPage.html", {  "form":form1 })


def destroyImage(request, id):
    destroy = Portfolio(id)
    destroy.delete()
    
    return redirect('portfolio')



# def newFilter(request):

#     dataFilter = Filter.objects.all()

#     if request.method == 'POST':
#         form = filterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('portfolio')
#     else:
#         form = filterForm()
#     return render(request,"crudProject/back/portfolio.html", {"dataFilter" : dataFilter, })


def destroyFilter(request, id):
    destroy = Filter(id)
    destroy.delete()
    
    return redirect('portfolio')
