from django.forms import forms,ModelForm
from  .models import  UserInfo

class UserForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'pas']
