# Generated by Django 2.0.2 on 2018-02-09 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0005_contactsdetail_bcc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactsdetail',
            options={'default_permissions': (), 'verbose_name': '联系人项目分组详情表', 'verbose_name_plural': '联系人项目分组详情表'},
        ),
        migrations.AlterModelOptions(
            name='groupsdetail',
            options={'default_permissions': (), 'verbose_name': '用户项目分组详情表', 'verbose_name_plural': '用户项目分组详情表'},
        ),
    ]
