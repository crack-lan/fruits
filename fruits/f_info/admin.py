from django.contrib import admin
from .models import *

class FruTypeAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id','ttitle']
class FruInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id','ftitle','fprice','funit','fclick','fstock','fabstract','ftype','isRecommend']
admin.site.register(FruType,FruTypeAdmin)
admin.site.register(FruInfo,FruInfoAdmin)