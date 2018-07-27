from django.db import models

class UserInfo(models.Model):
    uid=models.CharField(max_length=20,verbose_name="用户名")
    upwd=models.CharField(max_length=40,verbose_name="用户密码")
    uemail=models.CharField(max_length=30,verbose_name="用户邮箱")
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.uid

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'


class DeliveredInfo(models.Model):
    dname=models.CharField(max_length=20,verbose_name="收货人姓名")
    daddress=models.CharField(max_length=100,verbose_name="收货地址")
    dphone=models.CharField(max_length=11,verbose_name="手机号")
    did=models.ForeignKey('UserInfo',verbose_name="用户名")
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.dname
    class Meta:
        verbose_name = '地址管理'
        verbose_name_plural = '地址管理'