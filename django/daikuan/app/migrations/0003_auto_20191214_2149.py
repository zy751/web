# Generated by Django 2.2.3 on 2019-12-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191210_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daikuan',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='编码号'),
        ),
    ]
