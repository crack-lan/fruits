from django.db import models
from f_user.models import *
from f_info.models import *


class FruCart(models.Model):
    cuser=models.ForeignKey(UserInfo,verbose_name="用户名")
    cfruit=models.ForeignKey(FruInfo,verbose_name="商品名称")
    count=models.IntegerField(verbose_name="商品数量")
    def __str__(self):
        return self.cuser.uid
    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = '购物车'