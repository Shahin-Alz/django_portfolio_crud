from django_seed import Seed
from .models import Skills

def skillrun():
    seeder = Seed.seeder()
    datas = [
        {"name": "HTML", "value":99 },
        {"name":"JAVASCRIPT", "value": 75 },
        {"name":"WORDPRESS/CMS", "value": 90 },
        {"name":"DJANGO", "value": 93 },
        {"name":"CSS", "value": 90 },
        {"name":"PHP", "value": 80 },
        {"name":"PHOTOSHOP", "value": 55 }
    ]
    for data in datas:
        seeder.add_entity(Skills, 1, data)
    print(seeder.execute())