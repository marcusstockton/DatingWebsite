# Generated by Django 3.1.3 on 2020-11-04 20:36

import biography.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0004_auto_20201104_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default=1, upload_to=biography.models.user_directory_path),
            preserve_default=False,
        ),
    ]
