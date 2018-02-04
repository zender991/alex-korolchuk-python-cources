# Generated by Django 2.0.2 on 2018-02-04 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='', max_length=100)),
                ('descendants', models.CharField(default='', max_length=100)),
                ('story_id', models.CharField(default='', max_length=100)),
                ('kids', models.TextField(default='')),
                ('score', models.IntegerField(default=0)),
                ('text', models.TextField(default='')),
                ('time', models.CharField(default='', max_length=100)),
                ('title', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=100)),
                ('url', models.URLField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Categories')),
            ],
        ),
    ]
