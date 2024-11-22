# Generated by Django 5.1.3 on 2024-11-22 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('slug', models.SlugField(max_length=25, unique=True)),
            ],
            options={
                'ordering': ['name'],
                'indexes': [models.Index(fields=['slug'], name='main_catego_slug_f935f9_idx')],
            },
        ),
        migrations.CreateModel(
            name='Celestial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('created', models.TimeField(auto_now_add=True)),
                ('updated', models.TimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='celestial')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImageCelestial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='celestial/%Y/%m/%d')),
                ('celestial', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.celestial', verbose_name='image')),
            ],
        ),
        migrations.AddIndex(
            model_name='celestial',
            index=models.Index(fields=['id', 'slug'], name='main_celest_id_6b95e4_idx'),
        ),
        migrations.AddIndex(
            model_name='celestial',
            index=models.Index(fields=['name'], name='main_celest_name_f6cb46_idx'),
        ),
    ]
