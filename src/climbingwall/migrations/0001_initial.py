# Generated by Django 3.0.2 on 2020-01-03 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Climbingwall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('logo', models.ImageField(blank=True, upload_to='', verbose_name='Логотип')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Город')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('url', models.URLField(blank=True, verbose_name='Веб-сайт')),
                ('kinds', models.ManyToManyField(related_name='climbingwalls', to='common.ClimbingKind')),
            ],
            options={
                'verbose_name': 'Скалодром',
                'verbose_name_plural': 'Скалодромы',
            },
        ),
        migrations.CreateModel(
            name='ClimbingwallPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('photo', models.ImageField(blank=True, upload_to='media/climbingwalls/', verbose_name='Фото')),
                ('climbingwall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='climbingwall.Climbingwall')),
            ],
            options={
                'verbose_name': 'Фотография скалодрома',
                'verbose_name_plural': 'Фотографии скалодрома',
            },
        ),
    ]
