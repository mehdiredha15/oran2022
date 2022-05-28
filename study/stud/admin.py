from django.contrib import admin

# Register your models here.
from .models import Room,Category,Stade,Classe,Payment,Coor

admin.site.register(Room)
admin.site.register(Category)
admin.site.register(Stade)
admin.site.register(Classe)
admin.site.register(Payment)
admin.site.register(Coor)
