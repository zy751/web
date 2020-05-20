from django.contrib import admin

from .models import Stuinfo,Teacher,shenq,daikuan,Register
# Register your models here.
# class StuInline(admin.TabularInline):
#     model =shenq
class StuAdmin(admin.ModelAdmin):
    list_display = ['StuNum','StuName','stuid']
    search_fields = ['StuNum','stuid']
class TeaAdmin(admin.ModelAdmin):
    list_display = ['TeaNum','TeaName','Tel']
    search_fields = ['TeaNum','TeaName']

# class huankuanAdmin(admin.ModelAdmin):
#     list_display = ['num', 'time', 'status']
#     search_fields = ['num', 'status']

class shenqAdmin(admin.ModelAdmin):

    # Stunum=str(Stuinfo.objects.filter(shenq__pk='Stunum'))
    list_display = ['num','edu','time','Stunum']
    search_fields = ['edu', 'num','Stunum']
    # readonly_fields = ()
    # raw_id_fields = ["Forkey",]
class daikuanAdmin(admin.ModelAdmin):
    list_display = ['num','id','time']
    search_fields = ['num','id']

class RAdmin(admin.ModelAdmin):
    list_display = ['username','password','name']
    search_fields = ['username']

admin.site.register(Stuinfo,StuAdmin)
admin.site.register(Teacher,TeaAdmin)
admin.site.register(shenq,shenqAdmin)
admin.site.register(daikuan,daikuanAdmin)
admin.site.register(Register,RAdmin)

