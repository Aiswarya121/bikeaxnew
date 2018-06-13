# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-13 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_auto_20180420_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=20)),
                ('phonenumber', models.IntegerField(default=0)),
                ('Email', models.CharField(blank=True, max_length=30)),
                ('PermanentAddress', models.TextField(max_length=50)),
                ('TemporaryAddress', models.TextField(max_length=50)),
                ('City', models.CharField(blank=True, max_length=20)),
                ('State', models.CharField(blank=True, max_length=20)),
                ('Landmark', models.CharField(blank=True, max_length=30)),
                ('Pincode', models.IntegerField(default=0)),
            ],
        ),
    ]