from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from f_user.models import *
from f_order.models import *
from f_user import login_confirm
from f_cart.models import *
from django.db import transaction
from datetime import datetime
import time
from django.http import JsonResponse,HttpResponse
import requests
import json


@login_confirm.login
def place(request,idss=0,num=0):
    user=UserInfo.objects.get(id=request.session['user_id'])
    if idss==0:
        get=request.GET
        fruit_ids=get.getlist('id')
        cart_id=[int(item) for item in fruit_ids]
        cart=FruCart.objects.filter(cuser_id=user.id).filter(cfruit_id__in=cart_id)
    else:
        cart1=FruCart.objects.filter(cuser_id=user.id).get(cfruit_id=idss)
        cart1.count=int(num)
        cart1.save()
        fruit_ids=[idss]
        cart=FruCart.objects.filter(cuser_id=user.id).filter(cfruit=idss)
    deliveres=DeliveredInfo.objects.filter(did_id=request.session['user_id'])
    content = {'switch': 3,'deliver':deliveres,'title':'提交订单','btitle':'提交订单','cart':cart,'user':user,'fruit_ids':','.join(fruit_ids)}
    return render(request,'f_order/place_order.html',content)


@transaction.atomic()
@login_confirm.login
def order_create(request):
    tran=transaction.savepoint()
    fruit_ids=request.POST.get('f_ids')
    fruit_id = [int(item) for item in fruit_ids.split(',')]
    try:
        order=OrderInfo()
        now=datetime.now()
        user_id=request.session['user_id']
        order.onumber=int(str(int(time.time()))+str(user_id))
        print(order.onumber)
        order.ouser=UserInfo.objects.get(id=user_id)
        order.odate=now
        order.ototal=request.POST.get('total')
        address=DeliveredInfo.objects.get(id=request.POST.get('address'))
        order.oaddress='地址:'+address.daddress+'收货人:'+address.dname+'手机号:'+address.dphone
        order.opaystyle=request.POST.get('paystyle')
        order.save()
        for fid in fruit_id:
            detail=OrderDetail()
            detail.order=order
            cart=FruCart.objects.get(cfruit_id=fid,cuser__id=user_id)
            fruit=FruInfo.objects.get(id=fid)
            print(fruit.fstock,cart.count)
            if fruit.fstock >= cart.count:
                fruit.fstock=fruit.fstock-cart.count
                fruit.save()
                detail.fruit=FruInfo.objects.get(id=fruit.id)
                detail.count=cart.count
                detail.price=fruit.fprice
                detail.save()
                cart.delete()
            else:
                transaction.savepoint_rollback(tran)
                return redirect('/cart/')
        transaction.savepoint_commit(tran)
        if order.opaystyle == 'cash':
            return redirect('/user/order/')
        else:
            print(order.onumber)
            return redirect('/order/pay/' + str(order.onumber) + '/')
    except Exception as e:
        print('=================={}'.format(e))
        transaction.savepoint_rollback(tran)



@login_confirm.login
def order_pay(request,onum=0):
    dict={}
    if request.is_ajax():
        time.sleep(0.5)
        if OrderInfo.objects.get(onumber=int(onum)).ostatus==1:
            dict['ok']=1
        else:
            dict['ok']=0
        return JsonResponse(dict)
    else:
        if request.method=='GET':
            order=OrderInfo.objects.get(onumber=int(onum))
            return render(request,'f_order/order_pay.html',{'title':'收银台','switch':3,'btitle':'收银台','order':order})
        elif request.method=='POST':
            onu=request.POST.get('onums')
            try:
                order=OrderInfo.objects.get(onumber=int(onu))
                order.ostatus=1
                order.save()
                return redirect('/user/order/')
            except Exception as e:
                print('=================={}'.format(e))
                return redirect('/order/pay/',onums=onu)


@csrf_exempt
@login_confirm.login
def change_pay(request):
    pay=request.POST.get('pay_style')
    onu=request.POST.get('onum')
    pays=OrderInfo.objects.get(onumber=int(onu))
    data={}
    try:
        pays.opaystyle=pay
        pays.save()
        data['ok']=1
    except Exception as e:
        data['ok']=0
    return JsonResponse(data)


@login_confirm.login
def order_remind(request,onum):
    data={}
    order=OrderInfo.objects.get(onumber=onum)
    try:
        if order.isRemind==False:
            order.isRemind=True
            order.save()
            data['ok']='提醒成功'
        else:
            data['ok'] = '管理员已收到您的提醒，无需再次提醒'
    except Exception as e:
        data['ok']='请稍后再试'
    return JsonResponse(data)


@login_confirm.login
def order_logistics(request,onum):
    lnum=Logistics.objects.get(order_id=onum).lnumber
    type=Logistics.objects.get(order_id=onum).lname.epy
    print(lnum,type)
    url = 'http://www.kuaidi100.com/query?type={}&postid={}'.format(type,lnum)
    # 发送请求
    rs = requests.get(url)
    kd_info = json.loads(rs.text)
    msg = kd_info['message']
    if msg == 'ok':
        data = kd_info['data']
        return render(request,'f_order/express.html',{'title':'快递查询','switch':3,'btitle':'快递信息','data':data})
    else:
        return render(request,'f_order/express.html',{'title':'快递查询','switch':3,'btitle':'快递信息','data':'查询快递出错!'})


@login_confirm.login
def order_confirm(request,onum):
    data={}
    try:
        order=OrderInfo.objects.get(onumber=onum)
        order.ostatus=3
        order.save()
        data['ok']=1
    except Exception as e:
        data['ok']=0
    return JsonResponse(data)


@login_confirm.login
def order_appraise(request,onum):
    fruits=OrderDetail.objects.filter(order_id=onum)
    return  render(request,'f_order/evaluate.html',{'title': '订单评价', 'switch': 3, 'btitle': '商品评价','fruits':fruits,'onum':onum})


@login_confirm.login
def order_evaluate(request):
    onum=request.POST.get('onum')
    fruits=OrderDetail.objects.filter(order_id=onum)
    for fruit in fruits:
        ids=fruit.fruit_id
        star=request.POST.get('evalue'+str(ids))
        text=request.POST.get('text'+str(ids))
        value=Evaluate()
        value.date=datetime.now()
        value.euser_id=request.session['user_id']
        value.efruit_id=int(ids)
        value.star=int(star)
        value.value=text
        value.save()
    order=OrderInfo.objects.get(onumber=onum)
    order.ostatus=4
    order.save()
    return redirect('/user/order/')


@login_confirm.login
def order_del(request,onum):
    OrderInfo.objects.get(onumber=onum).delete()
    return redirect('/user/order/')