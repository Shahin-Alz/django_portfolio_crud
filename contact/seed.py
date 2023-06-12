from django_seed import Seed
from .models import Contact

def runContact():
    seeder = Seed.seeder()
    datas = [
        {
        "location": "A108 Adam Street, New York, NY 535022", 
        "mail":"info@example.com", 
        "phone": 1558955451 },
        
        
    ]
    for data in datas:
        seeder.add_entity(Contact, 1, data)
    print(seeder.execute())