from django.contrib import admin
from .models import *

class LogisticsInline(admin.StackedInline):
    model = Logistics
    extra = 1

class EvaluateAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['euser', 'efruit','star','value','date']


class OrderInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['onumber','status','oaddress','odate','isRemind']
    inlines = [LogisticsInline]
    search_fields = ['ostatus']


admin.site.register(OrderInfo,OrderInfoAdmin)
admin.site.register(ExpressInfo)
admin.site.register(Evaluate,EvaluateAdmin)
