from django import forms
from .models import Stuinfo
# 继承forms.Form
class LoginForm(forms.Form):
  # 如果为空则报错
  username = forms.CharField(required=True)
  # 同时也可以设定长度限制min_length、max_length
  password = forms.CharField(required=True, min_length=5)
class StuinfoForm(forms.Form):
  StuNum = forms.CharField(max_length=8, required=True)
  StuName = forms.CharField(max_length=20, required=True)
  Sex = forms.CharField(max_length=2, required=True)
  department = forms.CharField(max_length=20,required=True)
  stuid = forms.CharField(max_length=18, required=True)
  Tel = forms.CharField(max_length=12)
  major = forms.CharField(max_length=20)
  email = forms.EmailField(required=False)
class daikuanForm(forms.Form):
  StuNum = forms.CharField(max_length=8, required=True)
  edu=forms.IntegerField(required=True)
class TeainfoForm(forms.Form):
  TeaNum = forms.CharField(max_length=8, required=True)
  TeaName = forms.CharField(max_length=20, required=True)
  Tel = forms.CharField(max_length=12)
  Sex = forms.CharField(max_length=2, required=True)
class shenhForm(forms.Form):
  TeaNum=forms.CharField(max_length=8,required=True)
  num=forms.IntegerField(required=True)


