# Generated by Django 4.2.6 on 2023-10-29 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobster', '0002_user_id_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='adminname',
            field=models.EmailField(max_length=100),
        ),
    ]
