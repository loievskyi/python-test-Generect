from django.contrib import admin

from .models import Company, Person


admin.site.register(Person)
admin.site.register(Company)
