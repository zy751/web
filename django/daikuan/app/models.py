from django.db import models

# Create your models here.
class Stuinfo(models.Model):
    StuNum=models.CharField(max_length=8,primary_key=True,verbose_name='学号')
    StuName=models.CharField(max_length=20,verbose_name='姓名')
    Sex=models.CharField(max_length=2,choices=(('W','女'),('M','男')),verbose_name='性别')
    department=models.CharField(max_length=20,choices=(('L','理工部'),('W','文艺部'),('G','管理部'),('J','经济系')),verbose_name='系别')
    stuid=models.CharField(max_length=18,verbose_name='身份证')
    Tel=models.CharField(max_length=12,verbose_name='电话')
    major=models.CharField(verbose_name='专业',max_length=20)
    email=models.EmailField(verbose_name='邮箱',blank=True,help_text='可不填')
    def __str__(self):
        return self.StuNum
    class Meta:
        verbose_name='学生信息'
        verbose_name_plural='学生信息'

class Teacher(models.Model):
    TeaNum=models.CharField(max_length=8,primary_key=True,verbose_name='职工号')
    TeaName=models.CharField(max_length=20,verbose_name='姓名')
    Tel=models.CharField(max_length=12,verbose_name='电话')
    sex = models.CharField(max_length=2,choices=(('W', '女'), ('M', '男')), verbose_name='性别')
    def __str__(self):
        return self.TeaNum
    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'

class shenq(models.Model):
    # models=Stuinfo
    num = models.AutoField(primary_key=True,verbose_name='预编码号')
    Stunum=models.ForeignKey(Stuinfo,on_delete=models.CASCADE,verbose_name='学号')
    time=models.DateTimeField(verbose_name='申请时间',auto_now=True)
    edu = models.IntegerField(default=10000, verbose_name='贷款额度')
    status=models.IntegerField(default=0,verbose_name='审批状态')
    def __str__(self):
        return str(self.num)
    class Meta:
        verbose_name = '贷款申请信息'
        verbose_name_plural = '贷款申请信息'

class daikuan(models.Model):
    num=models.OneToOneField(shenq,verbose_name='预编码号',on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True,verbose_name='编码号')
    TeaNum=models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='职工号')
    time=models.DateTimeField(verbose_name='审批时间',auto_now=True)
    status = models.IntegerField(default=0, verbose_name='还款状态')
    need = models.IntegerField(default=0,verbose_name='所需还款')
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '贷款信息'
        verbose_name_plural = '贷款信息'


class Register(models.Model):
   username = models.CharField(max_length = 32,verbose_name = '学号',)
   password = models.CharField(max_length = 32,verbose_name = '密码',default='jianghuai')
   name=models.CharField(max_length=20,verbose_name='姓名',default='')
   email = models.EmailField(verbose_name = '注册邮箱',blank=True,help_text='可不填')
   phone_number = models.CharField(max_length = 14,verbose_name = '电话号码',blank=True)
   class Meta:
       verbose_name_plural='账号管理'
       verbose_name='账号管理'

