# Generated by Django 2.2.3 on 2020-01-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200130_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='daikuan',
            name='need',
            field=models.IntegerField(default=0, verbose_name='所需还款'),
        ),
    ]