from django_seed import Seed
from .models import Portfolio
from .models import Filter

def runPortfolio():
    seeder = Seed.seeder()
    datas = [
        {
            "name": "app", 
            "image": "/static/assets/img/portfolio/portfolio-1.jpg", 
            
        },
        {
            "name": "web", 
            "image": "/static/assets/img/portfolio/portfolio-2.jpg", 
            
        },
        {
            "name": "app", 
            "image": "/static/assets/img/portfolio/portfolio-3.jpg", 
            
        },
        {
            "name": "card", 
            "image": "/static/assets/img/portfolio/portfolio-4.jpg", 
            
        },
        {
            "name": "web", 
            "image": "/static/assets/img/portfolio/portfolio-5.jpg", 
            
        },
        {
            "name": "app", 
            "image": "/static/assets/img/portfolio/portfolio-6.jpg", 
            
        },
        {
            "name": "card", 
            "image": "/static/assets/img/portfolio/portfolio-7.jpg", 
            
        },
        {
            "name": "card", 
            "image": "/static/assets/img/portfolio/portfolio-8.jpg", 
            
        },
        {
            "name": "web", 
            "image": "/static/assets/img/portfolio/portfolio-9.jpg", 
            
        },
    ]
    for data in datas:
        seeder.add_entity(Portfolio, 1, data)
    print(seeder.execute())




def runFilter():
    seeder = Seed.seeder()
    datas = [
        {
            "name": "all", 
            
            
        },
        {
            "name": "app", 
            
            
        },
        {
            "name": "web", 
            
            
        },
        {
            "name": "card", 
            
            
        },
    
    ]
    for data in datas:
        seeder.add_entity(Filter, 1, data)
    print(seeder.execute())