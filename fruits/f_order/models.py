from django.db import models


class OrderInfo(models.Model):
    onumber=models.CharField(max_length=20,primary_key=True,verbose_name="订单号")
    ouser=models.ForeignKey('f_user.UserInfo',verbose_name="用户名")
    odate=models.DateTimeField(verbose_name="订单时间")
    ostatus=models.IntegerField(default=0,verbose_name="订单状态")
    opaystyle=models.CharField(max_length=20,verbose_name="付款方式")
    ototal=models.DecimalField(max_digits=6,decimal_places=2,verbose_name="订单金额")
    oaddress=models.CharField(max_length=150,verbose_name="收货地址")
    isRemind=models.BooleanField(default=False,verbose_name='是否提醒')
    def __str__(self):
        return self.onumber

    def status(self):
        if self.ostatus==0:
            if self.opaystyle!='cash':
                return '未支付'
            else:
                return '货到付款，未发货'
        elif self.ostatus==1:
            return '已支付，未发货'
        elif self.ostatus==2:
            return '已发货，未收货'
        elif self.ostatus==3:
            return '已收货，未评价'
        elif self.ostatus == 4:
            return '订单已完成'
        elif self.ostatus == 5:
            return '已发货'

    status.short_description = '订单状态'

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = '订单信息'


class OrderDetail(models.Model):
    fruit=models.ForeignKey('f_info.FruInfo')
    order=models.ForeignKey('OrderInfo')
    price=models.DecimalField(max_digits=5,decimal_places=2)
    count=models.IntegerField()


class ExpressInfo(models.Model):
    ename=models.CharField(max_length=20,verbose_name="快递名称")
    epy=models.CharField(max_length=20,verbose_name="快递代码")
    def __str__(self):
        return self.ename
    class Meta:
        verbose_name='快递物流'
        verbose_name_plural = '快递物流'


class Logistics(models.Model):
    order=models.ForeignKey('OrderInfo',verbose_name="订单号")
    lnumber=models.CharField(max_length=20,verbose_name="物流单号")
    lname=models.ForeignKey('ExpressInfo',verbose_name="物流名称")
    ldate=models.DateTimeField(auto_now=True,verbose_name="添加时间")
    is_Delete=models.BooleanField(default=False)
    def __str__(self):
        return self.order.onumber

    class Meta:
        verbose_name = '发货信息'
        verbose_name_plural = '发货信息'


class Evaluate(models.Model):
    euser=models.ForeignKey('f_user.UserInfo',verbose_name="用户名")
    efruit=models.ForeignKey('f_info.FruInfo',verbose_name="商品名")
    star=models.IntegerField(default=5,verbose_name="评分")
    value=models.CharField(max_length=1000,verbose_name="评论内容")
    date=models.DateTimeField(auto_now=True,verbose_name="评论时间")
    def __str__(self):
        return self.euser.uid

    class Meta:
        verbose_name = '商品评价'
        verbose_name_plural = '商品评价'
