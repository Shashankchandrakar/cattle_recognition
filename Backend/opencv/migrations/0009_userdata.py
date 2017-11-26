# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opencv', '0008_user_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencv.user')),
            ],
        ),
    ]
