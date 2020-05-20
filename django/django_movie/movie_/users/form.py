from django import forms

class Userform(forms.Form):
    username=forms.CharField(required=True)
    pwd=forms.CharField(required=True)