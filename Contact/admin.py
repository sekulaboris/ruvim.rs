from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display=('subject','email','message')
    list_filter=('email','subject')
    search_fields=('subject','message')
    ordering=('-email',)