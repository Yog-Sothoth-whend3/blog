from django.contrib import admin
from.models import article,user
# Register your models here.
class artcleconsole(admin.ModelAdmin):
    list_display = ['pk','title','context','date','aemail','ISdelete']

class userconsole(admin.ModelAdmin):
    list_display = ['username','email','password','ISdelete']




admin.site.register(article,artcleconsole)
admin.site.register(user,userconsole)