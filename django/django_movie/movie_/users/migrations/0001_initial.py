# Generated by Django 2.2.3 on 2020-04-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=20, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户名')),
                ('sex', models.CharField(choices=[('W', '女'), ('M', '男')], max_length=2, verbose_name='性别')),
                ('email', models.EmailField(blank=True, help_text='可不填', max_length=254, verbose_name='邮箱')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]