from django.db import models

# Create your models here.


class Drug(models.Model):
    """药品"""
    name = models.CharField(max_length=20, verbose_name='药品名称')
    image = models.ImageField(upload_to='drug', verbose_name='药品图片')
    num = models.CharField(max_length=10,verbose_name='药品编号')
    d_type = models.CharField(max_length=20, choices=(('0','处方药'),('1','非处方')), verbose_name='药品类型')
    status = models.CharField(max_length=20, choices=(('0','销售中'),('1','已停售')))
    describe = models.CharField(max_length=100, verbose_name='药品描述')
    PurchasingPrice = models.CharField(max_length=100,verbose_name='进价')
    SellingPrice = models.CharField(max_length=100,verbose_name='售价')
    Stock = models.CharField(max_length=100, verbose_name='库存')
    surplus = models.CharField(max_length=100, verbose_name='剩余量')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')


class ProjectManager(models.Model):
    name = models.CharField(max_length=100,verbose_name='收费项目名称')
    num = models.CharField(max_length=100, verbose_name='收费项目编号')
    price = models.CharField(max_length=100, verbose_name='收费价格')

