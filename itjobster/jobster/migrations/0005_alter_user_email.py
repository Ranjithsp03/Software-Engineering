# Generated by Django 4.2.6 on 2023-11-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobster', '0004_resume_remove_user_id_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
