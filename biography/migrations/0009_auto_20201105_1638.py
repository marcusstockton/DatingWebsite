# Generated by Django 3.1.3 on 2020-11-05 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0008_auto_20201105_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
    ]
