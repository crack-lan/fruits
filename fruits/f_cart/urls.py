from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.cart),
    url(r'^add(\d+)_(\d+)/$',views.cart_add),
    url(r'^alter(\d+)_(\d+)/$',views.cart_alter),
    url(r'^del(\d+)/$',views.cart_del),
    url(r'^count/$',views.count),

]