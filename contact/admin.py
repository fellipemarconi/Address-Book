from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'first_name', 'last_name', 'email', 'phone', 'created_date',)
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = ('id', 'first_name', 'last_name', 'email',)
    list_per_page = 25
    list_max_show_all = 100
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = 'id',
    list_per_page = 15