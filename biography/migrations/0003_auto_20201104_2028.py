# Generated by Django 3.1.3 on 2020-11-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0002_auto_20201104_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='line2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
