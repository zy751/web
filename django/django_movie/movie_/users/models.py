from django.db import models
# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=20,primary_key=True,verbose_name='用户名')
    pwd=models.CharField(max_length=255,verbose_name='密码')
    def __str__(self):
        return self.username
class Userinfo(models.Model):
    username=models.CharField(max_length=20,primary_key=True,verbose_name='用户名')
    sex=models.CharField(max_length=2,choices=(('W','女'),('M','男')),verbose_name='性别')
    email=models.EmailField(help_text='可不填',verbose_name='邮箱',blank=True)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name='用户信息'
        verbose_name_plural='用户信息'

class Movie(models.Model):
    title = models.CharField(max_length=60,verbose_name='标题')
    href = models.CharField(max_length=150, verbose_name='播放地址')
    imgsrc = models.CharField(max_length=150, verbose_name='图片链接')
    author=models.CharField(max_length=60,verbose_name='导演')
    pers=models.CharField(max_length=255,verbose_name='主演')
    area=models.CharField(max_length=40,verbose_name='地区')
    year=models.CharField(max_length=10,verbose_name='年份')
    mes=models.CharField(max_length=2000,verbose_name='简介')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='电影'
        verbose_name='电影'

class Comic(models.Model):
    title = models.CharField(max_length=60, verbose_name='标题')
    href = models.CharField(max_length=150, verbose_name='播放地址')
    imgsrc = models.CharField(max_length=150, verbose_name='图片链接')
    author = models.CharField(max_length=60, verbose_name='导演')
    pers = models.CharField(max_length=255, verbose_name='主演')
    area = models.CharField(max_length=40, verbose_name='地区')
    year = models.CharField(max_length=10, verbose_name='年份')
    mes = models.CharField(max_length=2000, verbose_name='简介')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = '动漫'
        verbose_name = '动漫'

class Variety(models.Model):
    title = models.CharField(max_length=60,verbose_name='标题')
    href = models.CharField(max_length=150, verbose_name='播放地址')
    imgsrc = models.CharField(max_length=150, verbose_name='图片链接')
    author=models.CharField(max_length=60,verbose_name='导演')
    pers = models.CharField(max_length=255, verbose_name='主演')
    area=models.CharField(max_length=40,verbose_name='地区')
    year=models.CharField(max_length=10,verbose_name='年份')
    mes=models.CharField(max_length=2000,verbose_name='简介')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='综艺'
        verbose_name='综艺'

class Sitcom(models.Model):
    title = models.CharField(max_length=60,verbose_name='标题')
    href = models.CharField(max_length=150, verbose_name='播放地址')
    imgsrc = models.CharField(max_length=150, verbose_name='图片链接')
    author=models.CharField(max_length=60,verbose_name='导演')
    pers = models.CharField(max_length=255, verbose_name='主演')
    area=models.CharField(max_length=40,verbose_name='地区')
    year=models.CharField(max_length=10,verbose_name='年份')
    mes=models.CharField(max_length=2000,verbose_name='简介')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='连续剧'
        verbose_name='连续剧'
