# Generated by Django 5.1.1 on 2024-09-13 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GradeLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(upload_to='covers/')),
                ('publisher', models.CharField(max_length=200)),
                ('book_type', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=200)),
                ('publication_year', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('edited_by', models.CharField(max_length=200)),
                ('fgos', models.BooleanField(default=False)),
                ('education_level', models.CharField(max_length=100)),
                ('publication_place', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('view_count', models.IntegerField(default=0)),
                ('short_name', models.SlugField(unique=True)),
                ('grade_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='textbooks.gradelevel')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='textbooks.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('image_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('folder', models.CharField(max_length=100)),
                ('solution_text', models.TextField()),
                ('name1', models.CharField(blank=True, max_length=100, null=True)),
                ('name2', models.CharField(blank=True, max_length=100, null=True)),
                ('textbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='textbooks.textbook')),
            ],
        ),
    ]
