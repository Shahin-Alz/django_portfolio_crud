"""
URL configuration for crudProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from home.views import *
from about.views import *
from skills.views import *
from portfolio.views import *
from services.views import *
from testimonial.views import *
from contact.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('all/', alll, name='all'),
    
    path("about/", updateAbout, name="update"),

    path("skills/", newSkills, name="skills"),
    path("skills/destroy/<int:id>", destroySkills),
    # path("skills/", update, name="skills"),

    path("portfolio/", portfolio, name="portfolio"),
    path("portfolio/createImage", newImage, name="createImage"),
    path("portfolio/createFilter", newFilter, name="createFilter"),
    path("portfolio/destroyI/<int:id>", destroyImage),
    path("portfolio/destroyF/<int:id>", destroyFilter),

    path("services/", newService, name="services"),


    path("testimonial/", testimonial, name="testimonial"),
    path("testimonial/newTestimonial", newTestimonial, name="newTestimonial"),
    path("testimonial/destroy/<int:id>", destroyTestimonial),


    path("contact/", updateContact, name="contact"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
