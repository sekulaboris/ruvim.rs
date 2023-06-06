from django.contrib import admin
from .models import Onama

#----------- onama --------------------------
@admin.register(Onama)

class OnamaAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','publish','status')
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=('status','publish')



# Register your models here.
