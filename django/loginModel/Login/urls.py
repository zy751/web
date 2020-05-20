from django.urls import path
from django.conf.urls import url
from . import  views
app_name='user'
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('register/',views.regis,name='reg'),
    path('logout/',views.Logout,name='logout'),
    path('update/',views.update,name='update'),
    path('index/',views.index,name='index'),
    path('findp/',views.findPas,name='findP'),
]