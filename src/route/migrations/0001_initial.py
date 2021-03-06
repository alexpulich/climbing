# Generated by Django 3.0.2 on 2020-01-04 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('climbingwall', '0001_initial'),
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('grade', models.CharField(choices=[('5a', '5a'), ('5a+', '5a+'), ('5b', '5b'), ('5b+', '5b+'), ('5c', '5c'), ('5c+', '5c+'), ('6a', '6a'), ('6a+', '6a+'), ('6b', '6b'), ('6b+', '6b+'), ('6c', '6c'), ('6c+', '6c+'), ('7a', '7a'), ('7a+', '7a+'), ('7b', '7b'), ('7b+', '7b+'), ('7c', '7c'), ('7c+', '7c+'), ('8a', '8a'), ('8a+', '8a+'), ('8b', '8b'), ('8b+', '8b+'), ('8c', '8c'), ('8c+', '8c+'), ('9a', '9a'), ('9a+', '9a+'), ('9b', '9b'), ('9b+', '9b+'), ('9c', '9c'), ('9c+', '9c+')], max_length=3)),
                ('marker', models.CharField(max_length=100)),
                ('rank', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to=settings.AUTH_USER_MODEL)),
                ('climbingwall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='climbingwall.Climbingwall')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='common.ClimbingKind')),
            ],
            options={
                'verbose_name': 'Трасса',
                'verbose_name_plural': 'Трассы',
            },
        ),
        migrations.CreateModel(
            name='RoutePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('photo', models.ImageField(upload_to='media/routes/')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='route.Route')),
            ],
            options={
                'verbose_name': 'Фотография трассы',
                'verbose_name_plural': 'Фотографии трассы',
            },
        ),
    ]
