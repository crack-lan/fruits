from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.place),
    url(r'^remind/(\d+)/$',views.order_remind),
    url(r'^pay/(\d+)/$',views.order_pay),
    url(r'^pay/$',views.order_pay),
    url(r'^logistics/(\d+)/$',views.order_logistics),
    url(r'^confirm/(\d+)/$',views.order_confirm),
    url(r'^appraise/(\d+)/$',views.order_appraise),
    url(r'^evaluate/$',views.order_evaluate),
    url(r'^create/$',views.order_create),
    url(r'^place(\d+)_(\d+)/$',views.place),
    url(r'^change_pay/$',views.change_pay),
    url(r'^del/(\d+)/$',views.order_del),
]