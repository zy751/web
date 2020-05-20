from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import Userform
from .models import *
import hashlib
import random
from django.core import paginator
# Create your views here.
def is_login(req):
    return req.session.get('user',False)

def index(req):
    left=[]
    a=random.randint(0,296)
    movie=Movie.objects.all()[a:a+5]
    sit=Sitcom.objects.all()[a:a+5]
    comic=Comic.objects.all()[a:a+5]
    variety=Variety.objects.all()[a:a+5]
    left.extend(movie)
    left.extend(sit)
    left.extend(comic)
    left.extend(variety)
    res=left[4:16]
    first=res[1]
    return render(req, 'users/index.html', {'left':left,'first':first,'tui':res,'islogin':False})

def center(req):
    if(is_login(req)):
        return HttpResponse('hi')
    else:
        return redirect('users:login')

def logindex(req):
    print(req.session.get('user'))
    if(is_login(req)):
        left = []
        a = random.randint(0, 296)
        movie = Movie.objects.all()[a:a + 5]
        sit = Sitcom.objects.all()[a:a + 5]
        comic = Comic.objects.all()[a:a + 5]
        variety = Variety.objects.all()[a:a + 5]
        left.extend(movie)
        left.extend(sit)
        left.extend(comic)
        left.extend(variety)
        res = left[4:16]
        first = res[1]
        return render(req, 'users/index.html', {'left': left, 'first': first, 'tui': res, 'islogin': True})
    else:
        return redirect('users:login')

def login(req):
    if(req.method=='GET'):
        return render(req,'users/login.html')
    else:
        uf=Userform(req.POST)
        if(uf.is_valid()):
            username=uf.cleaned_data['username']
            psd=uf.cleaned_data['pwd']
            h1=hashlib.md5()
            h1.update(psd.encode('utf-8'))
            pwd=h1.hexdigest()
            if(user.objects.filter(username=username)):
                if(user.objects.filter(username=username,pwd=pwd)):
                    req.session['user']=username
                    return redirect('users:logindex')
                else:
                    msg='密码错误'
                    return render(req,'users/login.html',{'msg2':msg})
            else:
                msg = '账户不存在'
                return render(req, 'users/login.html', {'msg1': msg})

def register(req):
    if(req.method=='GET'):
        return render(req,'users/register.html')
    else:
        uf=Userform(req.POST)
        if (uf.is_valid()):
            username = uf.cleaned_data['username']
            if(user.objects.filter(username=username)):
                msg='用户名已存在'
                return render(req,'users/register.html',{'msg':msg})
            else:
                pwd = uf.cleaned_data['pwd']
                h1=hashlib.md5()
                h1.update(pwd.encode(encoding='utf-8'))
                newpwd=h1.hexdigest()
                user.objects.create(username=username,pwd=newpwd).save()
                return redirect('users:login')

def logout(req):
    req.session.delete()
    return redirect('users:login')

def comic(req):
    datas = Comic.objects.all()
    page = paginator.Paginator(datas, 30)
    if(req.GET.get('page',None)):
        index=int(req.GET.get('page'))
    else:
        index=1
    pag = page.page(index)
    print(pag)
    return render(req, 'users/video.html', {'datas':pag})
def movie(req):
    datas = Movie.objects.all()
    page = paginator.Paginator(datas, 30)
    if(req.GET.get('page',None)):
        index=int(req.GET.get('page'))
    else:
        index=1
    pag = page.page(index)
    return render(req, 'users/video.html', {'datas': pag})
def sitcom(req):
    datas=Sitcom.objects.all()
    page=paginator.Paginator(datas,30)
    if (req.GET.get('page', None)):
        index = int(req.GET.get('page'))
    else:
        index = 1
    pag=page.page(index)
    return render(req, 'users/video.html', {'datas':pag})
def variety(req):
    datas=Variety.objects.all()
    page=paginator.Paginator(datas,30)
    if(req.GET.get('page',None)):
        index=int(req.GET.get('page'))
    else:
        index=1
    pag=page.page(index)
    return render(req, 'users/video.html', {'datas':pag})

# def video(req,kind,index):
#     print(kind)
#     if kind=='movie':
#         datas=Movie.objects.all()
#     elif kind=='sitcom':
#         datas=Sitcom.objects.all()
#     elif kind=='variety':
#         datas=Variety.objects.all()
#     elif kind=='comic':
#         datas=Comic.objects.all()
#     page=paginator.Paginator(datas,30)
#     if index=='':
#         index=1
#     pag=page.page(index)
#     return render(req, 'users/video.html', {'datas':pag})

def search(req):
    keyword=req.GET.get('keyword')
    datas=[]
    datas.extend(Movie.objects.filter(title__contains=keyword))
    datas.extend(Sitcom.objects.filter(title__contains=keyword))
    datas.extend(Variety.objects.filter(title__contains=keyword))
    datas.extend(Comic.objects.filter(title__contains=keyword))
    page = paginator.Paginator(datas, 30)
    if(req.GET.get('page',None)):
        index=int(req.GET.get('page'))
    else:
        index=1
    pag = page.page(index)
    return render(req, 'users/video.html', {'datas': pag,'keyword':keyword})

