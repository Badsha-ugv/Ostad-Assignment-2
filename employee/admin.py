from django.contrib import admin

from .models import Employee 


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'phone']
    readonly_fields = ['salary', 'designation'] # block changing value from admin 
    search_fields = ['name', 'phone', 'designation']
    list_filter = ['designation', ]

admin.site.register(Employee, EmployeeAdmin)