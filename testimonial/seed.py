from django_seed import Seed
from .models import Testimonial

def runTestimonial():
    seeder = Seed.seeder()
    datas = [
        {
        "description": " Lorem, ipsum dolor sit amet consectetur adipisicing elit. Maxime, illum! Dignissimos suscipit amet sapiente possimus, placeat exercitationem saepe blanditiis pariatur id asperiores. Dolores, asperiores praesentium.", 
        "photo":"/static/assets/img/testimonials/testimonials-1.jpg", 
        "name":"Saul Goodman",
        "title":"CEO" },

        {
        "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Maxime, illum! Dignissimos suscipit amet sapiente possimus, placeat exercitationem saepe blanditiis pariatur id asperiores. Dolores, asperiores praesentium.", 
        "photo":"/static/assets/img/testimonials/testimonials-2.jpg",  
        "name":"Sarah Wilson",
        "title":"Designer" },

        {
        "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Maxime, illum! Dignissimos suscipit amet sapiente possimus, placeat exercitationem saepe blanditiis pariatur id asperiores. Dolores, asperiores praesentium.", 
        "photo":"/static/assets/img/testimonials/testimonials-3.jpg", 
        "name":"Jena Karlis",
        "title":"Store Owner" },

        {
        "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Maxime, illum! Dignissimos suscipit amet sapiente possimus, placeat exercitationem saepe blanditiis pariatur id asperiores. Dolores, asperiores praesentium.", 
        "photo":"/static/assets/img/testimonials/testimonials-4.jpg", 
        "name":"Matt Brandon",
        "title":"Freelancer" },

        {
        "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Maxime, illum! Dignissimos suscipit amet sapiente possimus, placeat exercitationem saepe blanditiis pariatur id asperiores. Dolores, asperiores praesentium.", 
        "photo":"/static/assets/img/testimonials/testimonials-5.jpg",  
        "name":"John Larson",
        "title":"Entrepreneur"  },

        
        
    ]
    for data in datas:
        seeder.add_entity(Testimonial, 1, data)
    print(seeder.execute())