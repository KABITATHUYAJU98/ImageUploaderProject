from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image) #Image lai register garem
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo', 'date'] #id--auto generate