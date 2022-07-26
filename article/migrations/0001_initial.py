# Generated by Django 4.0.6 on 2022-07-26 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

from article.gen_master_data import gen_master


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='삭제 날짜')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('hashtags', models.TextField(verbose_name='태그 내용')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
            ],
            options={
                'verbose_name': '게시글',
                'verbose_name_plural': '게시글',
                'db_table': 'article',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ArticleLikedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '좋아요',
                'verbose_name_plural': '좋아요',
                'db_table': 'like',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_liked_user',
            field=models.ManyToManyField(related_name='liked_article', through='article.ArticleLikedUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tag.tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(gen_master),
    ]