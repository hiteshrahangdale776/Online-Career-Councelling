from django.contrib import admin

from .models import Register

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
       list_display = [field.name for field in Register._meta.get_fields()]
    #    list_display=("Name","Emailid")
    