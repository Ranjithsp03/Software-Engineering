# Generated by Django 4.2.6 on 2023-10-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(max_length=100)),
                ('adminpass', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('gstin', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('companyname', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contact', models.BigIntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('aadhar', models.BigIntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
