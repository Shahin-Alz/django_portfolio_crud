from django_seed import Seed
from .models import Services

def runServices():
    seeder = Seed.seeder()
    datas = [
        {"titre": "Lorem Ipsum", "description":"Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident", "icon":"bi-briefcase" },
        {"titre":"Dolor Sitema", "description": "Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata", "icon":"bi-card-checklist" },
        {"titre":"Sed ut perspiciatis", "description": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur", "icon":"bi-bar-chart" },
        {"titre":"Magni Dolores", "description": "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum", "icon":"bi-binoculars" },
        {"titre":"Nemo Enim", "description": "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque", "icon":"bi-brightness-high" },
        {"titre":"Eiusmod Tempor", "description": "Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi", "icon":"bi-calendar4-week" },
        
    ]
    for data in datas:
        seeder.add_entity(Services, 1, data)
    print(seeder.execute())