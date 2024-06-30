from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'location']

admin.site.register(Lead, LeadAdmin)
