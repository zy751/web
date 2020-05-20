from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required

from .form import UserForm

from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

@login_required()
@permission_required('Login.add_userinfo')
def index(req):
    print(req.user.get_all_permissions())
    return render(req,'Login/index.html')

def login_view(req):
    if req.method == 'GET':
        return render(req, 'Login/login.html')
    elif req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pas']
            user = authenticate(req, username=username, password=pwd)
            if user is not None:
                login(req, user)
                return redirect('user:index')
            else:
                err = '账户或密码错误'
                messages.add_message(req,messages.ERROR,err)
                return redirect('user:login')
        return redirect('user:login')

def regis(req):
    if req.method == 'GET':
        return render(req, 'Login/register.html')
    elif req.method == 'POST':
        username = req.POST.get('username')
        pwd = req.POST.get('pwd')
        res = User.objects.filter(username=username)
        if( res ):
            err = '账户名已存在'
            messages.add_message(req,messages.ERROR,err)
            return redirect('user:reg')
        else:
            User.objects.create_user(username=username, email=None, password=pwd).save()
            messages.add_message(req, messages.SUCCESS, 'hello')
            return redirect('user:login')

def Logout(req):
    logout(req)
    messages.add_message(req,messages.SUCCESS,'logout success')
    return redirect('user:login')

def update(req):
    if req.method=='GET':
        return render(req,'Login/update.html')
    elif req.method=='POST':
        user=req.POST.get('username')
        pwd=req.POST.get('oldpwd')
        newpwd=req.POST.get('newpwd')
        if(authenticate(username=user,password=pwd)):
            u=User.objects.get(username=user)
            u.set_password(newpwd)
            u.save()
            messages.add_message(req,messages.SUCCESS,'修改密码成功，请重新登录')
            return redirect('user:login')
        else:
            err='账户或密码错误'
            messages.add_message(req,messages.ERROR,err)
            return redirect('user:update')

def findPas(req):
    if req.method=='GET':
        return render(req,'Login/reloadP.html')
    elif req.method=='POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        from_email=settings.DEFAULT_FROM_EMAIL
        if(User.objects.filter(username=username)):
            res=send_mail(f'{username}，修改密码','link：""',from_email,[email],fail_silently=True)
            print(res)
            success='修改密码邮件已发送至邮箱，请注意查收'
            messages.add_message(req,messages.SUCCESS,res)
            return redirect('user:login')
        else:
            err='该用户不存在'
            messages.add_message(req,messages.ERROR,err)
            return redirect('user:findP')




