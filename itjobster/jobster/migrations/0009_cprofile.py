# Generated by Django 4.2.6 on 2023-11-16 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobster', '0008_company_cid_alter_company_gstin_postjob'),
    ]

    operations = [
        migrations.CreateModel(
            name='cprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=255)),
                ('cwebsite', models.URLField(default='https://')),
                ('clocations', models.TextField()),
                ('jpostername', models.CharField(max_length=255)),
                ('jposterdesignation', models.CharField(max_length=255)),
                ('jposteremail', models.EmailField(max_length=254)),
                ('jposterphone', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobster.company')),
            ],
        ),
    ]
