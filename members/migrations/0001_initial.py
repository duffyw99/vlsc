# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-06-27 01:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('recruit_class', models.CharField(max_length=3)),
                ('member_photo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='MemberContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_street', models.CharField(max_length=250)),
                ('member_city', models.CharField(max_length=250)),
                ('member_state', models.CharField(max_length=250)),
                ('member_zip', models.CharField(max_length=250)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
            ],
        ),
    ]
