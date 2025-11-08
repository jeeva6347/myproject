from django.contrib import admin
from .models import *
# Register your models here.

class Baseadmin(admin.ModelAdmin):
    list_display=("fullname",
                  "profession",
                  "email",
                  "mobilenumber",
                  "city","address",
                  "status",
                  "creationdate",
                  "updated_at",
                  "profile",
    )
    list_per_page=5
admin.site.register(Directory,Baseadmin)




