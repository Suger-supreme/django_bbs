# Generated by Django 2.0 on 2019-09-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190917_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(default='avatars/default.png', upload_to='avatars/', verbose_name='头像'),
        ),
    ]
