# Generated by Django 4.2.6 on 2023-11-16 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobster', '0009_cprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cprofile',
            name='cid',
        ),
    ]