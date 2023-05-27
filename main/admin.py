from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class AccountAdmin(UserAdmin):
    list_display= ('username' , 'email' , 'dob', 'height', 'weight', 'extype', 'gender','veg')
    search_fields= ('username' , 'email')
    readonly_fields= ()
    
    filter_horizontal = ()
    list_filter=()
    fieldsets=()
    
admin.site.register(account, AccountAdmin)    
# Register your models here.
admin.site.register(recipe)
admin.site.register(nutpar)
admin.site.register(hcondition)

admin.site.register(recipe1)

admin.site.register(test)
admin.site.register(history)
admin.site.register(suser)