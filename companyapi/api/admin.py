from django.contrib import admin

# Register your models here.
from .models import Company,Employee
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','about','types')
    search_fields=('name',)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee)