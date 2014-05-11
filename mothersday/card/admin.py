from django.contrib import admin

from .models import Card

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email', 'major', 'attendance', 'interest', 'background', 'comments', 'created_at')
    list_filter = ('created_at',)
    ordering = ['-created_at']
    search_fields = ['name']

admin.site.register(Card, CardAdmin)
