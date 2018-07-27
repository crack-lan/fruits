from django.shortcuts import render
from .models import *
import random
from django.http import JsonResponse
from django.core.paginator import Paginator
from f_order.models import *
import zmail


def index(request):
    ftype=FruType.objects.filter(isDelete=False)
    type1=ftype[0]
    type2=ftype[1]
    type3=ftype[2]
    type4=ftype[3]
    type5=ftype[4]
    type6=ftype[5]
    new1=ftype[0].fruinfo_set.order_by('-id')[0:4]
    new2=ftype[1].fruinfo_set.order_by('-id')[0:4]
    new3=ftype[2].fruinfo_set.order_by('-id')[0:4]
    new4=ftype[3].fruinfo_set.order_by('-id')[0:4]
    new5=ftype[4].fruinfo_set.order_by('-id')[0:4]
    new6=ftype[5].fruinfo_set.order_by('-id')[0:4]
    hot1=ftype[0].fruinfo_set.order_by('fclick')[0:4]
    hot2=ftype[1].fruinfo_set.order_by('fclick')[0:4]
    hot3=ftype[2].fruinfo_set.order_by('fclick')[0:4]
    hot4=ftype[3].fruinfo_set.order_by('fclick')[0:4]
    hot5=ftype[4].fruinfo_set.order_by('fclick')[0:4]
    hot6=ftype[5].fruinfo_set.order_by('fclick')[0:4]
    recommend=FruInfo.objects.filter(isRecommend=True)
    adv_type1 = random.choice(ftype)
    adv_type2 = random.choice(ftype)
    while adv_type1==adv_type2:
        adv_type2=random.choice(ftype)
    adv1=random.choice(adv_type1.fruinfo_set.order_by('id'))
    adv2=random.choice(adv_type2.fruinfo_set.order_by('id'))
    while  adv1==adv2:
        adv2=random.choice(adv_type2.fruinfo_set.order_by('id'))

    con={'title':'首页','switch':1,'type1':type1,'type2':type2,'type3':type3,'type4':type4,'type5':type5,'type6':type6,'new1':new1,'new2':new2,'new3':new3,'new4':new4,'new5':new5,'new6':new6,'hot1':hot1,'hot2':hot2,'hot3':hot3,'hot4':hot4,'hot5':hot5,'hot6':hot6,'rec':recommend,'adv1':adv1,'adv2':adv2}
    return render(request,'f_info/index.html',con)


def list(request,tid,sort,page):
    ftype = FruType.objects.filter(isDelete=False)
    type1 = ftype[0]
    type2 = ftype[1]
    type3 = ftype[2]
    type4 = ftype[3]
    type5 = ftype[4]
    type6 = ftype[5]
    type=FruType.objects.filter(id=tid)[0]
    adv1=random.choice(type.fruinfo_set.order_by('id'))
    adv2=random.choice(type.fruinfo_set.order_by('id'))
    # while adv1 == adv2:
    #     adv2 = random.choice(type.fruinfo_set.order_by('id'))
    if sort=='1':
        list=type.fruinfo_set.order_by('-id')
    elif sort=='2':
        list=type.fruinfo_set.order_by('-fprice')
    elif sort=='3':
        list=type.fruinfo_set.order_by('-fclick')
    paginator=Paginator(list,15)
    pages=paginator.page(page)

    context={'title':type.ttitle,'switch':1,'type1':type1,'type2':type2,'type3':type3,'type4':type4,'type5':type5,'type6':type6,'pages':pages,'paginator':paginator,'type':type,'sort':sort,'adv1':adv1,'adv2':adv2}
    print(sort,tid,page)
    return render(request,'f_info/list.html',context)


def detail(request,fid,page=1):
    fruit=FruInfo.objects.filter(id=fid)[0]
    fruit.fclick=fruit.fclick+1
    fruit.save()
    type=FruType.objects.filter(ttitle=fruit.ftype)[0]
    ftype = FruType.objects.filter(isDelete=False)
    type1 = ftype[0]
    type2 = ftype[1]
    type3 = ftype[2]
    type4 = ftype[3]
    type5 = ftype[4]
    type6 = ftype[5]
    adv1 = random.choice(fruit.ftype.fruinfo_set.order_by('id'))
    adv2 = random.choice(fruit.ftype.fruinfo_set.order_by('id'))
    evaluate=Evaluate.objects.filter(efruit_id=fid)
    paginator = Paginator(evaluate, 15)
    pages = paginator.page(page)
    con={'title':fruit.ftype.ttitle,'switch':1,'pages':pages,'paginator':paginator,'type':type,'type1':type1,'type2':type2,'type3':type3,'type4':type4,'type5':type5,'type6':type6,'fruit':fruit,'adv1':adv1,'adv2':adv2,'id':fid}
    response = render(request,'f_info/detail.html',con)

    fruit_ids=request.COOKIES.get('fruit_ids','')
    fruit_id='{}'.format(fruit.id)
    if fruit_ids!='':
        fruit_ids1=fruit_ids.split(',')
        if fruit_ids1.count(fruit_id)>=1:
            fruit_ids1.remove(fruit_id)
        fruit_ids1.insert(0,fruit_id)
        if len(fruit_ids1)>=5:
            fruit_ids1.pop()
        fruit_ids=','.join(fruit_ids1)
    else:
        fruit_ids=fruit_id
    response.set_cookie('fruit_ids',fruit_ids)
    return response

