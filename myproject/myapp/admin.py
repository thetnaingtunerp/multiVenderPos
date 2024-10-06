from django.contrib import admin
from myapp.models import *
# Register your models here.
class branchadmin(admin.ModelAdmin):
    list_display = ('id','usr','branch_name','created_at','updated_at')
admin.site.register(branch,branchadmin)

class categoryadmin(admin.ModelAdmin):
    list_display = ('id','usr','branch','category','created_at','updated_at')
admin.site.register(category,categoryadmin)