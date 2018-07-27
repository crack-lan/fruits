from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1
from django.http import *
from . import login_confirm
from f_info.models import *
from f_order.models import *
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import zmail


def register(request):
    return render(request,'f_user/register.html')


def register_handle(request):
    #获取用户提交数据
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('pwd')
    cpwd=post.get('cpwd')
    uemail=post.get('email')
    #验证两次密码是否一致
    if upwd!=cpwd:
        return redirect('/user/register/')
    user = UserInfo()
    user.uid=uname
    user.uemail=uemail
    ss=sha1()
    ss.update(upwd.encode('utf-8'))
    ss2=ss.hexdigest()
    #密码加密
    user.upwd=ss2
    #存入数据库
    user.save()
    #转到登录界面
    return redirect('/user/login/')

def uname_exist(request):
    uname=request.GET.get('uname')
    exist=UserInfo.objects.filter(isDelete=False,uid=uname).count()
    return JsonResponse({'exist':exist})


def login(request):
    uname=request.COOKIES.get('uname','')
    context={'title':'用户登录','error_name':0,'error_pwd':'0','uname':uname}
    return render(request, 'f_user/login.html',context=context)


def login_handle(request):
    request.session.set_expiry(0)
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    remeber=post.get('remeber',0)
    user=UserInfo.objects.filter(isDelete=False).filter(uid=uname)
    if len(user)==1:
        sha=sha1()
        sha.update(upwd.encode('utf-8'))
        if sha.hexdigest()==user[0].upwd:
            url=request.COOKIES.get('url','/index/')
            if url!='/user/findpwd/':
                red=HttpResponseRedirect(url)
            else:
                red=HttpResponseRedirect('/index/')
            if remeber!=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uanme','',max_age=-1)
            request.session['user_id']=user[0].id
            request.session['user_name']=user[0].uid
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': '1', 'uname': uname,'upwd':upwd}
            return render(request, 'f_user/login.html', context=context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': '0', 'uname': uname, 'upwd': upwd}
        return render(request, 'f_user/login.html', context=context)


def exit(request):
    request.session.flush()
    return redirect('/index/')


@login_confirm.login
def user_info(request):
    info = UserInfo.objects.filter(uid=request.session.get('user_name'))[0]
    fruit_ids = request.COOKIES.get('fruit_ids','')
    fruits = []
    if fruit_ids!='':
        fruit_ids1=fruit_ids.split(',')
        for fruit_id in fruit_ids1:
            fruit = FruInfo.objects.filter(id = int(fruit_id))[0]
            fruits.append(fruit)
    return render(request,'f_user/user_center_info.html',{'title':'个人信息','switch':2,'mes':1,'info':info,'fruits':fruits,'btitle':'用户中心'})


@login_confirm.login
def order(request,page=1):
    f_order=OrderInfo.objects.filter(ouser=request.session['user_id']).order_by('-odate')
    for o in f_order:
        if o.ostatus==1:
            if Logistics.objects.filter(is_Delete=False).filter(order=o):
                o.ostatus=2
                o.save()
        elif o.ostatus==0:
            if Logistics.objects.filter(is_Delete=False).filter(order=o):
                o.ostatus=5
                o.save()
    paginator=Paginator(f_order,5)
    pages=paginator.page(page)
    return render(request,'f_user/user_center_order.html',{'title':'我的订单','paginator':paginator,'pages':pages,'switch':2,'mes':2,'btitle':'我的订单','f_order':f_order})


@login_confirm.login
def address(request):
    adds = DeliveredInfo.objects.filter(isDelete=False).filter(did=request.session.get('user_id',''))
    if adds != '':
        return render(request,'f_user/user_center_address.html',{'title':'收货地址','switch':2,'mes':3,'adds':adds,'btitle':'地址管理'})


@login_confirm.login
def address_add(request):
    post= request.POST
    deliver=DeliveredInfo()
    deliver.dname=post.get('re_name','')
    deliver.daddress=post.get('detail_add','')
    deliver.dphone=post.get('phone_num','')
    deliver.did=UserInfo.objects.filter(id=request.session.get('user_id',''))[0]
    deliver.save()
    return redirect('/user/address/')


@login_confirm.login
def address_del(request):
    DeliveredInfo.objects.get(id=request.GET.get('address','')).delete()
    return redirect('/user/address/')


def find_pwd(request):
    return render(request,'f_user/findpwd.html')


@csrf_exempt
def reset_pwd(request):
    post=request.POST
    user=post.get('user')
    print(user)
    dict={}
    if(UserInfo.objects.filter(uid=user)):
        u=UserInfo.objects.get(uid=user)
        if post.get('email')==u.uemail:
            newpwd=post.get('newpwd')
            s1 = sha1()
            s1.update(newpwd.encode('utf-8'))
            s2 = s1.hexdigest()
            # 密码加密
            u.upwd=s2
            u.save()
            dict['ok']=2
        else:
            dict['ok']=1
    else:
        dict['ok']=0
    return JsonResponse(dict)