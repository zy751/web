# Generated by Django 2.2.3 on 2019-12-10 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stuinfo',
            old_name='sex',
            new_name='Sex',
        ),
    ]
