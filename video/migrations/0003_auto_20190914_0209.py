# Generated by Django 2.2.5 on 2019-09-14 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20190913_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
