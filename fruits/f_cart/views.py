from django.shortcuts import render,redirect
from .models import *
from f_user.models import *
from f_user import login_confirm
from django.http import JsonResponse

@login_confirm.login
def cart(request):
    user_id=request.session['user_id']
    fruits = FruCart.objects.filter(cuser__id=user_id)
    return render(request,'f_cart/cart.html',{'title':'购物车','switch':3,'btitle':'购物车','fruits':fruits})

@login_confirm.login
def cart_add(request,fid,count):
    uid = request.session['user_id']
    fid=int(fid)
    count=int(count)
    fcart=FruCart.objects.filter(cuser__id=uid,cfruit_id=fid)
    if len(fcart)>=1:
        fcart=fcart[0]
        fcart.count=fcart.count+count
    else:
        fcart=FruCart()
        fcart.cuser_id=uid
        fcart.cfruit_id=fid
        fcart.count=count
    fcart.save()
    if request.is_ajax():
        count=FruCart.objects.filter(cuser__id=request.session['user_id']).count()

        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')


@login_confirm.login
def cart_alter(request,cart_id,count):
    try:
        cart=FruCart.objects.filter(cuser__id=request.session['user_id']).get(cfruit_id=cart_id)
        cart.count=int(count)
        cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok':1}
    return JsonResponse(data)


@login_confirm.login
def cart_del(request,cart_id):
    try:
        cart=FruCart.objects.filter(cuser__id=request.session['user_id']).get(cfruit_id=cart_id)
        cart.delete()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)


def count(request):
    if request.session.has_key('user_id'):
        counts=FruCart.objects.filter(cuser__id=request.session['user_id']).count()
    else:
        counts=0
    return JsonResponse({'count':counts})

