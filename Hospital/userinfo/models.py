from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Patients(models.Model):
    """
    病人表（挂号信息表）
    """
    name = models.CharField(max_length=10, verbose_name='姓名')
    IdCard = models.CharField(max_length=18, verbose_name='身份证号码')
    SocialSsecurity = models.CharField(max_length=20, verbose_name='社保号码', null=True, blank=True)  # 该字段可以为空
    RegistrationFee = models.IntegerField(verbose_name='挂号费')
    tel = models.CharField(max_length=11, verbose_name='联系电话')
    SelfPaying = models.CharField(max_length=10, choices=(('yes', '自费'), ('no', '非自费')), verbose_name='是否是自费')
    gender = models.CharField(max_length=10, choices=(('meal', '男'), ('femeal', '女')), verbose_name='性别')
    age = models.IntegerField(default=0, null=True, blank=True, verbose_name='年龄')
    job = models.CharField(max_length=50, null=True, blank=True, default='', verbose_name='职业')
    jude = models.CharField(max_length=10, choices=(('0', '初诊'), ('1', '复诊')), verbose_name='初复诊')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')
    RegistrationTime = models.DateTimeField(auto_now_add=True, verbose_name='挂号时间')
    status = models.CharField(max_length=10, choices=(('0', '已挂号'), ('1', '已住院'), ('2', '已出院'), ('3', '已退号')))
    p_number = models.CharField(max_length=13, verbose_name='病历号')  # 手机号加一位
    nurse = models.CharField(max_length=200, verbose_name='护理', blank=True, null=True)
    bed_num = models.CharField(max_length=10, blank=True, null=True, verbose_name='床位号')
    cash = models.CharField(max_length=200, blank=True, null=True, verbose_name='押金')
    illness = models.CharField(max_length=300, blank=True, null=True, verbose_name='病情')
    doctor = models.ForeignKey('Doctor',on_delete=models.SET_DEFAULT,default='秦韬')
    P_office_fk = models.ForeignKey('Office',on_delete=models.SET_DEFAULT,default='妇科')
    manager = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name='收费项目')
    manager_time = models.DateTimeField(auto_now=True)


class DrugNum(models.Model):
    need_num = models.IntegerField(verbose_name='所需药品数量')
    get_num = models.IntegerField(verbose_name='已发药品数量')
    p_fk = models.ForeignKey('Patients',on_delete=models.CASCADE,verbose_name='病人')



class Doctor(models.Model):
    """医生"""
    name = models.CharField(max_length=20, verbose_name='医生姓名')
    IdCard = models.CharField(max_length=18, verbose_name='身份证号码')
    tel = models.CharField(max_length=11, verbose_name='联系电话')
    tel_2 = models.CharField(max_length=11, verbose_name='座机')
    gender = models.CharField(max_length=10, choices=(('meal', '男'), ('femeal', '女')), verbose_name='性别')
    birthday = models.DateField(verbose_name='生日')
    age = models.IntegerField(default=0, null=True, blank=True, verbose_name='年龄')
    email = models.EmailField(verbose_name='电子邮箱')
    education = models.CharField(max_length=100,
                                 choices=(('0', '本科'), ('1', '研究生'), ('2', '博士'), ('3', '院士'), ('4', '海归')))
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')
    D_office_fk = models.ForeignKey('Office',on_delete=models.SET_DEFAULT,default='妇科')


class Office(models.Model):
    """科室"""
    name = models.CharField(max_length=100, verbose_name='科室名称')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class UserProfile(AbstractUser):
    really_name = models.CharField(max_length=100, verbose_name='真实姓名')
    role = models.IntegerField(verbose_name='角色')
    jurisdiction = models.CharField(max_length=100, verbose_name='挂号信息管理')
    jurisdiction1 = models.CharField(max_length=100, verbose_name='门诊医生管理',)
    jurisdiction2 = models.CharField(max_length=100, verbose_name='药品管理')
    jurisdiction3 = models.CharField(max_length=100, verbose_name='住院办理')
    jurisdiction4 = models.CharField(max_length=100, verbose_name='收费项目登记')
    jurisdiction5 = models.CharField(max_length=100, verbose_name='在院发药')
    jurisdiction6 = models.CharField(max_length=100, verbose_name='住院结算')
    jurisdiction7 = models.CharField(max_length=100, verbose_name='月营业额统计')
    jurisdiction8 = models.CharField(max_length=100, verbose_name='年营业额统计')
    jurisdiction9 = models.CharField(max_length=100, verbose_name='用户管理')
    jurisdiction10 = models.CharField(max_length=100, verbose_name='角色管理')
    jurisdiction11 = models.CharField(max_length=100, verbose_name='资源管理')
