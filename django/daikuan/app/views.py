from django.shortcuts import render,redirect,HttpResponse,render_to_response,HttpResponseRedirect
from .models import Register,Teacher,Stuinfo,shenq,daikuan
from .form import LoginForm,StuinfoForm,daikuanForm,TeainfoForm,shenhForm
from django.core import paginator
from datetime import datetime
import cgi
def shouye(request):
    return  render(request, 'app/common/index.html')

def logout(request):
    request.COOKIES['username']=None
    response=render(request, 'app/common/login.html')
    return response

def login(request):
    return render(request,'app/common/login.html')
def is_login(req):
    number = req.COOKIES.get('username')
    if number==None:
        return redirect('app:login')

def index(request):
    if request.method == "POST":
        uf = LoginForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userResult = Register.objects.filter(username=username, password=password)
            teaR = Teacher.objects.filter(TeaNum=username, Tel=password)
            # pdb.set_trace()
            if (len(userResult) > 0):
                stu = Stuinfo.objects.filter(StuNum=username)
                if len(stu):
                    stu=Stuinfo.objects.get(StuNum=username)
                    response = render(request, 'app/base/base_stu.html', {'stu': stu})
                    response.set_cookie('username', username, 3600)
                else:
                    name=Register.objects.get(username=username)
                    response = render(request, 'app/base/base_stu.html', {'name': name})
                    response.set_cookie('username', username, 3600)
                return response
            if (len(teaR) > 0):
                tea = Teacher.objects.get(TeaNum=username)
                response = render(request, 'app/base/base_tea.html', {'tea': tea})
                response.set_cookie('username', username, 3600)
                return response
            else:
                error_msg = '用户名或密码错误'
                response = render(request, 'app/common/login.html', {'error_msg': error_msg})
                return response
        else:
                error_msg = '用户名或密码错误'
                response = render(request, 'app/common/login.html', {'error_msg': error_msg})
                return response
    if request.COOKIES.get('username'):
        username=request.COOKIES.get('username')
        userResult = Register.objects.filter(username=username)
        teaR = Teacher.objects.filter(TeaNum=username)
        if (len(userResult) > 0):
            stu = Stuinfo.objects.filter(StuNum=username)
            if len(stu):
                stu = Stuinfo.objects.get(StuNum=username)
                response = render(request, 'app/base/base_stu.html', {'stu': stu})
                response.set_cookie('username', username, 3600)
            else:
                name = Register.objects.get(username=username)
                response = render(request, 'app/base/base_stu.html', {'name': name})
                response.set_cookie('username', username, 3600)
            return response
        if (len(teaR) > 0):
            tea = Teacher.objects.get(TeaNum=username)
            response = render(request, 'app/base/base_tea.html', {'tea': tea})
            response.set_cookie('username', username, 3600)
            return response

    else:
        return redirect('app:login')

def stuinfo(request):
    #判断有无登录
    number=request.COOKIES.get('username')
    if number:
        #判断有无信息
        stu=Stuinfo.objects.filter(StuNum=number)
        if len(stu)>0:
            stu=Stuinfo.objects.get(StuNum=number)
            return render(request, 'app/student/stuinfo.html', {'stu':stu})
        else:
            return redirect('app:upload')
    else:
        return render(request, 'app/common/login.html')

def upload(req):
    number = req.COOKIES.get('username')
    if number:
        name = Register.objects.get(username=number)
        if req.method=='POST':
            uf=StuinfoForm(req.POST)
            if uf.is_valid():
                StuNum=uf.cleaned_data['StuNum']
                StuName=uf.cleaned_data['StuName']
                sex = uf.cleaned_data['Sex']
                department = uf.cleaned_data['department']
                stuid = uf.cleaned_data['stuid']
                Tel=uf.cleaned_data['Tel']
                major = uf.cleaned_data['major']
                email = uf.cleaned_data['email']
                A=Stuinfo.objects.create(StuName=StuName,StuNum=StuNum,Sex=sex,department=department,stuid=stuid,Tel=Tel,major=major,email=email)
                A.save()
                return redirect('app:stuinfo')
            else:
                return render(req, 'app/student/upload.html', {'name':name})
        else:
            return render(req, 'app/student/upload.html', {'name':name})
    else:
        return redirect('app:login')

def change(req):
    number = req.COOKIES.get('username')
    if number:
        if Register.objects.filter(username=number):
            if req.method=='POST':
                uf=StuinfoForm(req.POST)
                if uf.is_valid():
                    StuNum=uf.cleaned_data['StuNum']
                    StuName=uf.cleaned_data['StuName']
                    sex = uf.cleaned_data['Sex']
                    department = uf.cleaned_data['department']
                    stuid = uf.cleaned_data['stuid']
                    Tel=uf.cleaned_data['Tel']
                    major = uf.cleaned_data['major']
                    email = uf.cleaned_data['email']
                    Stuinfo.objects.filter(StuNum=StuNum).update(StuName=StuName,StuNum=StuNum,Sex=sex,department=department,stuid=stuid,Tel=Tel,major=major,email=email)
                    return redirect('app:stuinfo')
                else:
                    return redirect('app:stuinfo')
            else:
                return redirect('app:stuinfo')
        else:
            if req.method=='POST':
                uf=TeainfoForm(req.POST)
                if uf.is_valid():
                    TeaNum=uf.cleaned_data['TeaNum']
                    TeaName=uf.cleaned_data['TeaName']
                    Tel=uf.cleaned_data['Tel']
                    Sex=uf.cleaned_data['Sex']
                    print(TeaNum,TeaName,Tel,Sex)
                    Teacher.objects.filter(TeaNum=TeaNum).update(TeaName=TeaName,TeaNum=TeaNum,Tel=Tel,sex=Sex)
                    return redirect('app:teainfo')
                else:
                    return redirect('app:teainfo')
            else:
                return redirect('app:teainfo')
    else:
        return redirect('app:login')

def daikuanshenq2(req):
    number = req.COOKIES.get('username')
    if number:
        stu = Stuinfo.objects.filter(StuNum=number)
        stu = Stuinfo.objects.get(StuNum=number)
        stunum=stu.StuNum
        exist=shenq.objects.filter(Stunum=stunum,status=0)
        if exist:
            err='已经申请，等待审批'
            return render(req,'app/base/base_stu.html',{'stu':stu,'err':err})
        return render(req, 'app/student/daikuanshenq.html', {'stu': stu})
    else:
        return redirect('app:login')

def daikuanshenq(req):
    number = req.COOKIES.get('username')
    if number:
        stu = Stuinfo.objects.filter(StuNum=number)
        try:
            Stusq=shenq.objects.filter(Stunum=number)
        except:
            Stusq=''
        if len(stu)>0 and len(Stusq)==0:
            stu = Stuinfo.objects.get(StuNum=number)
            return render(req, 'app/student/daikuanshenq.html',{'stu':stu})
        elif len(stu)>0 and len(Stusq)>0:
            mes='已经申请过了,点击查看申请结果'
            mes2='继续申请'
            stu = Stuinfo.objects.get(StuNum=number)
            return render(req,'app/base/base_stu.html',{'mes':mes,'stu':stu,'mes2':mes2})
        else:
            error_msg='请完善个人信息,点击去完善'
            return render(req,'app/base/base_stu.html',{'error_msg':error_msg})
    else:
        return redirect('app:login')

def submit(req):
    number = req.COOKIES.get('username')
    stu = Stuinfo.objects.get(StuNum=number)
    if req.method == 'POST':
        uf=daikuanForm(req.POST)
        if uf.is_valid():
            edu=uf.cleaned_data['edu']
            A=shenq.objects.create(Stunum=stu,edu=edu)
            A.save()
            return redirect('app:index')
        else:
            return redirect('app:daikuanshenq')

def teainfo(req):
    number = req.COOKIES.get('username')
    if number:
        tea=Teacher.objects.get(TeaNum=number)
        return render(req, 'app/teacher/teainfo.html', {'tea':tea})
    else:
        return redirect('app:login')

def allinfo(req,index):
    number=req.COOKIES.get('username')
    if number:
        list=Stuinfo.objects.order_by('StuNum')
        pag=paginator.Paginator(list,10)
        if index=='':
            index=1
        page=pag.page(index)
        tea=Teacher.objects.get(TeaNum=number)
        return render(req,'app/teacher/allinfo.html',{'page':page,'tea':tea})
    else:
        return redirect('app:login')

def daikuanshenp(req,index):
    number = req.COOKIES.get('username')
    if number:
        tea = Teacher.objects.get(TeaNum=number)
        list=shenq.objects.filter(status=0).order_by('time')
        page=paginator.Paginator(list,10)
        page=page.page(index)
        return render(req,'app/teacher/daikuanshenp.html',{'page':page,'tea':tea})
    else:
        return redirect('app:login')

def detail(req,stunum):
    number = req.COOKIES.get('username')
    if number:
        tea = Teacher.objects.get(TeaNum=number)
        stu=Stuinfo.objects.get(StuNum=stunum)
        daikuan=shenq.objects.get(Stunum=stunum,status=0)
        return render(req,'app/teacher/detail.html',{"tea":tea,"stu":stu,"daikuan":daikuan})
    else:
        return redirect('app:login')

def shenh(req,Stunum):
    number = req.COOKIES.get('username')
    tea = Teacher.objects.get(TeaNum=number)
    if req.method == 'POST':
        uf = shenhForm(req.POST)
        if uf.is_valid():
            Tea = uf.cleaned_data['TeaNum']
            Teanum = Teacher.objects.get(TeaNum=Tea)
            nu=uf.cleaned_data['num']
            num =shenq.objects.get(num=nu)
            exist=daikuan.objects.filter(num__Stunum=Stunum)
            if len(exist)<=0:
                A = daikuan.objects.create(TeaNum=Teanum, num=num)
                A.save()
                need=daikuan.objects.get(TeaNum=Teanum, num=num).num.edu
                shenq.objects.filter(Stunum=Stunum).update(status=1)
            else:
                new=shenq.objects.get(Stunum=Stunum,status=0)
                newsqedu=new.edu
                newsqtime=new.time
                old=shenq.objects.get(Stunum=Stunum,status=1).edu
                A=daikuan.objects.get(num__Stunum=Stunum)
                time=A.time
                newtime=datetime.now()
                newneed=int(((newtime.year-time.year)*12+newtime.month-time.month)*old*0.01+old)+newsqedu
                shenq.objects.filter(Stunum=Stunum,status=1).update(edu=old+newsqedu,time=newsqtime)
                num =shenq.objects.get(Stunum=Stunum,status=1)
                shenq.objects.get(Stunum=Stunum,status=0).delete()
                exist.delete()
                A = daikuan.objects.create(TeaNum=Teanum, num=num)
                A.save()
                daikuan.objects.filter(TeaNum=Teanum, num=num).update(need=newneed)

            return redirect('app:index')
        else:
            return render(req,'app/teacher/daikuanshenp.html',{'tea':tea})

def tuihui(req,Stunum):
    number = req.COOKIES.get('username')
    tea = Teacher.objects.get(TeaNum=number)
    if tea:
        shenq.objects.filter(Stunum=Stunum,status=0).delete()
    return redirect('app:index')

def daikuaninfo(req):
    number = req.COOKIES.get('username')
    if number:
        stu=Stuinfo.objects.filter(StuNum=number)
        if len(stu)>0:
            stu=Stuinfo.objects.get(StuNum=number)
            daik=daikuan.objects.filter(num__Stunum__StuNum=number)
            if daik:
                daik=daikuan.objects.get(num__Stunum__StuNum=number)
                if daik.status ==0:
                    return render(req, 'app/common/daikuaninfo.html',{'stu':stu,'daikuan':daik})
                else:
                    error_msg = '已还款'
                    return render(req, 'app/base/base_stu.html', {'stu': stu, 'erro_msg': error_msg})

            else:
                error_msg='暂未申请贷款,或申请未通过'
                return render(req,'app/base/base_stu.html',{'stu':stu,'erro_msg':error_msg})
        else:
            error_msg = '暂未申请贷款,或申请未通过'
            name=Register.objects.get(username=number)
            return render(req, 'app/base/base_stu.html', {'name':name,'erro_msg': error_msg})

    else:
        return redirect('app:login')

def daikuaninfo2(req,index):
    number = req.COOKIES.get('username')
    tea = Teacher.objects.filter(TeaNum=number)
    if len(tea) > 0:
        tea = Teacher.objects.get(TeaNum=number)
        list = daikuan.objects.filter(status=0).order_by('num__Stunum__StuNum')
        if list:
            page = paginator.Paginator(list, 10)
            page = page.page(index)
            return render(req, 'app/common/daikuaninfo2.html', {'tea': tea, 'page': page})
        else:
            error = '暂无贷款信息'
            return render(req, 'app/base/base_tea.html', {'tea': tea, 'error': error})
    else:
        return redirect('app:login')

def daikuandetail(req,Stunum):
    number = req.COOKIES.get('username')
    tea = Teacher.objects.get(TeaNum=number)
    daik=daikuan.objects.get(num__Stunum=Stunum)
    return render(req,'app/teacher/detail2.html',{'tea':tea,'daik':daik})

def huankuan(req,Stunum):
    number = req.COOKIES.get('username')
    tea = Teacher.objects.get(TeaNum=number)
    if len(req.POST['money'])==0:
        daikuan.objects.filter(num__Stunum=Stunum).update(status=1)
    else:
        old=daikuan.objects.get(num__Stunum=Stunum).need
        if old==0:
            old=shenq.objects.get(Stunum=Stunum)
            oldtime=old.time
            oldmoney=old.edu
            newtime=datetime.now()
            newneed=((newtime.year-oldtime.year)*12+newtime.month-oldtime.month)*oldmoney*0.01+oldmoney
            daikuan.objects.filter(num__Stunum=Stunum).update(need=newneed - int(req.POST['money']))
        else:
            daikuan.objects.filter(num__Stunum=Stunum).update(need=old-int(req.POST['money']))
        if daikuan.objects.get(num__Stunum=Stunum).need==0:
            daikuan.objects.filter(num__Stunum=Stunum).update(status=1)
    return render(req,'app/base/base_tea.html',{'tea':tea})

def admm(req):
    number = req.COOKIES.get('username')
    if number:
        tea = Teacher.objects.get(TeaNum=number)
        if req.method=='POST':
            num=req.POST['pn']
            for i in range(1,int(num)+1):
                una=req.POST['major']+req.POST['year']+req.POST['yx']+'%03d'%i
                Register.objects.create(username=una).save()
            return render(req,'app/teacher/adminchange.html',{'tea':tea})
        else:
            return render(req,'app/teacher/adminchange.html',{'tea':tea})
    else:
        return redirect('app:login')

def admm2(req):
    number = req.COOKIES.get('username')
    if number:
        tea = Teacher.objects.get(TeaNum=number)
        if req.method=='POST':
            num=req.POST['pn']
            for i in range(int(num)+1):
                una=req.POST['major']+req.POST['year']+req.POST['yx']+'%03d'%i
                Register.objects.filter(username=una).delete()
            return render(req,'app/teacher/adminchange.html',{'tea':tea})
        else:
            return render(req,'app/teacher/adminchange.html',{'tea':tea})
    else:
        return redirect('app:login')