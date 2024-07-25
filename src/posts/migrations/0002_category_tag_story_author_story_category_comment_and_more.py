# Generated by Django 5.0.7 on 2024-07-24 07:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.category'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('opinion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.opinion')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
                ('opinion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.opinion')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('opinion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.opinion')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(blank=True, to='posts.tag'),
        ),
    ]