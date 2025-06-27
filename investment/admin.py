from django.contrib import admin
from .models import BusinessIdea



@admin.register(BusinessIdea)
class BusinessIdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'status')
# Register your models here.
