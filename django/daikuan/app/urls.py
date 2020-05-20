from django.conf.urls import url
from django.urls import path
from django.contrib.auth import admin
from . import views
# from django.contrib.auth import views as auth_views
app_name='app'
urlpatterns = [
    url(r'^submit$',views.submit,name='submit'),
    url(r'^shouye$',views.shouye,name='shouye'),
    url(r'^index$', views.index,name='index'),
    url(r'^daikuaninfo$',views.daikuaninfo,name='daikuaninfo'),
    url(r'^alldaikuaninfo/(\d*)$',views.daikuaninfo2,name='daik2'),
    url(r'^stuinfo$',views.stuinfo,name='stuinfo'),
    url('^daikuanshenq$',views.daikuanshenq,name='daikuanshenq'),
    url(r'^login$', views.login,name='login'),
    url(r'^logout$', views.logout,name='logout'),
    url(r'^teainfo$',views.teainfo,name='teainfo'),
    url(r'^daikuanshenp/(\d*)$',views.daikuanshenp,name='daikuanshenp'),
    url(r'^upload$',views.upload,name='upload'),
    url(r'^change$',views.change,name='change'),
    url(r'^allstuinfo/(\d*)$',views.allinfo,name='allinfo'),
    url(r'^detail/([A-Z]{2}\d{6})$',views.detail,name='detail'),
    url(r'^shenh/(.*)$',views.shenh,name='shenh'),
    url(r'^daikuandetail/([A-Z]{2}\d{6})$',views.daikuandetail,name='dkdetail'),
    url(r'^tuihui/([A-Z]{2}\d{6})$',views.tuihui,name='tuihui'),
    url(r'^huankuan/([A-Z]{2}\d{6})$',views.huankuan,name='huankuan'),
    url(r'^daikuanshenq2$',views.daikuanshenq2,name='daikuanshenq2'),
    url(r'^addadm$',views.admm,name='addadm'),
    url(r'^deladm$',views.admm2,name='deladm'),
]