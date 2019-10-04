# Generated by Django 2.0 on 2019-09-17 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='article2tag',
            options={'verbose_name': '文章-标签', 'verbose_name_plural': '文章-标签'},
        ),
        migrations.AlterModelOptions(
            name='articledetail',
            options={'verbose_name': '文章详情', 'verbose_name_plural': '文章详情'},
        ),
        migrations.AlterModelOptions(
            name='articleupdown',
            options={'verbose_name': '文章点赞', 'verbose_name_plural': '文章点赞'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'blog站点', 'verbose_name_plural': 'blog站点'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '文章分类', 'verbose_name_plural': '文章分类'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.TextField(max_length=255, verbose_name='文章描述'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='articledetail',
            name='content',
            field=models.TextField(verbose_name='文章内容'),
        ),
    ]
