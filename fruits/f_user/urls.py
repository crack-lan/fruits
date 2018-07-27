from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^uname_exist/',views.uname_exist),
    url(r'^login/$',views.login),
    url(r'^login_handle/$',views.login_handle),
    url(r'^login_out/$',views.exit),
    url(r'^info/$',views.user_info),
    url(r'^order/(\d+)/$',views.order),
    url(r'^order/$',views.order),
    url(r'^address/$',views.address),
    url(r'^address_add/$',views.address_add),
    url(r'^address/del',views.address_del),
    url(r'^findpwd/$',views.find_pwd),
    url(r'^resetpwd/$',views.reset_pwd),
]