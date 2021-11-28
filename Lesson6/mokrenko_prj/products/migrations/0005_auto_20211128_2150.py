# Generated by Django 3.2.5 on 2021-11-28 18:50

import django.contrib.sites.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('products', '0004_auto_20211128_2112'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
        migrations.AlterModelManagers(
            name='good_item',
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
        migrations.RemoveField(
            model_name='good_item',
            name='site',
        ),
        migrations.AddField(
            model_name='good_item',
            name='site',
            field=models.ManyToManyField(related_name='site_rel_name', to='sites.Site'),
        ),
    ]
