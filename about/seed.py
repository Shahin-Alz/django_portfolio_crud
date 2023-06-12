from django_seed import Seed
from .models import About

def run():
    seeder = Seed.seeder()
    datas = [
        {
            "birthday": "1 May 1955", 
            "website": "www.example.com", 
            "phone": 1234567890, 
            "city": "New York, USA", 
            "age":30, 
            "degree":"Master", 
            "email":"email@example.com", 
            "freelance": "Available",
        }
    ]
    for data in datas:
        seeder.add_entity(About, 1, data)
    print(seeder.execute())


