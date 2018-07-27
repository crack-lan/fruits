from django.db import models
from tinymce.models import HTMLField


class FruType(models.Model):
    ttitle=models.CharField(max_length=20,verbose_name="类别名称")
    isDelete=models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle
    class Meta:
        verbose_name='水果分类'
        verbose_name_plural='水果分类'

class FruInfo(models.Model):
    ftitle=models.CharField(max_length=20,verbose_name="名称")
    fprice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="价格")
    fdetail=HTMLField(verbose_name="详情信息")
    ftype=models.ForeignKey('FruType',verbose_name="水果分类")
    fpic=models.ImageField(upload_to='f_media',verbose_name="水果图片")
    isDelete=models.BooleanField(default=False)
    funit=models.CharField(max_length=20,verbose_name="规格")
    fclick=models.IntegerField(verbose_name="点击数")
    fabstract=models.CharField(max_length=200,verbose_name="水果描述")
    fstock=models.IntegerField(verbose_name="库存")
    isRecommend=models.BooleanField(default=False,verbose_name="是否推荐")
    def __str__(self):
        return self.ftitle
    class Meta:
        verbose_name='水果信息'
        verbose_name_plural='水果信息'

