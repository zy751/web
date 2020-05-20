from . import views
from django.urls import path
from django.conf.urls import url

app_name='users'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logindex/',views.logindex,name='logindex'),
    path('logout/',views.logout,name='logout'),
    path('personcenter/',views.center,name='center'),
    # url('video/type=(.*?)&page=(\d*)$',views.video,name='video'),
    url('movie',views.movie,name='movie'),
    url('sitcom',views.sitcom,name='sitcom'),
    url('variety',views.variety,name='variety'),
    url('comic',views.comic,name='comic'),
    url('search',views.search,name='search')
]