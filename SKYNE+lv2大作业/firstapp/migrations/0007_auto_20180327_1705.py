# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-27 09:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0006_auto_20171209_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='belong_to',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='belong_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('normal', 'normal'), ('dislike', 'dislike'), ('like', 'like')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=5),
        ),
    ]
