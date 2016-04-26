# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('username', models.CharField(unique=True, max_length=40)),
                ('first_name', models.CharField(max_length=40, blank=True)),
                ('last_name', models.CharField(max_length=40, blank=True)),
                ('tagline', models.CharField(max_length=140, blank=True)),
                ('twitter_handle', models.CharField(max_length=20, blank=True)),
                ('facebook_username', models.CharField(max_length=50, blank=True)),
                ('linkedin_username', models.CharField(max_length=50, blank=True)),
                ('google_username', models.CharField(max_length=50, blank=True)),
                ('instagram_username', models.CharField(max_length=50, blank=True)),
                ('pintrest_username', models.CharField(max_length=50, blank=True)),
                ('personal_website', models.URLField(blank=True)),
                ('address_street', models.CharField(max_length=100, blank=True)),
                ('address_city', models.CharField(max_length=100, blank=True)),
                ('address_state', models.CharField(max_length=2, blank=True)),
                ('address_country', models.CharField(max_length=100, blank=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
