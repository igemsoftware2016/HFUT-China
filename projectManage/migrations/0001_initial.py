# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='functions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'bio_functions',
            },
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
                ('function', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projectManage.functions')),
            ],
            options={
                'db_table': 'bio_project',
            },
        ),
        migrations.CreateModel(
            name='tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'bio_tracks',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projectManage.tracks'),
        ),
    ]
