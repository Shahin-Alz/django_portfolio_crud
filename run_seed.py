import django
django.setup()

from about.seed import run
from skills.seed import skillrun
from portfolio.seed import runPortfolio
from portfolio.seed import runFilter
from services.seed import runServices
from testimonial.seed import runTestimonial
from contact.seed import runContact

if __name__== '__main__':
    run()
    skillrun()
    runPortfolio()
    runFilter()
    runServices()
    runTestimonial()
    runContact()