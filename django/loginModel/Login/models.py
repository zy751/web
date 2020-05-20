from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.

class UserInfo(models.Model):
    username=models.CharField(max_length=20,verbose_name='用户名')
    pas=models.CharField(max_length=20,verbose_name='密码')
    class Meta:
        db_table='Login_Userinfo'

