# Generated by Django 4.1.3 on 2023-11-16 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobster', '0013_postjob_cid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cprofile',
            name='cid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jobster.company'),
            preserve_default=False,
        ),
    ]
