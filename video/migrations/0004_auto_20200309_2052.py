# Generated by Django 2.2.6 on 2020-03-09 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20190914_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='path',
        ),
        migrations.AddField(
            model_name='video',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]