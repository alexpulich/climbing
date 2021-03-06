# Generated by Django 3.0.2 on 2020-01-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активная'),
        ),
        migrations.AlterField(
            model_name='route',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='route',
            name='grade',
            field=models.CharField(choices=[('5a', '5a'), ('5a+', '5a+'), ('5b', '5b'), ('5b+', '5b+'), ('5c', '5c'), ('5c+', '5c+'), ('6a', '6a'), ('6a+', '6a+'), ('6b', '6b'), ('6b+', '6b+'), ('6c', '6c'), ('6c+', '6c+'), ('7a', '7a'), ('7a+', '7a+'), ('7b', '7b'), ('7b+', '7b+'), ('7c', '7c'), ('7c+', '7c+'), ('8a', '8a'), ('8a+', '8a+'), ('8b', '8b'), ('8b+', '8b+'), ('8c', '8c'), ('8c+', '8c+'), ('9a', '9a'), ('9a+', '9a+'), ('9b', '9b'), ('9b+', '9b+'), ('9c', '9c'), ('9c+', '9c+')], max_length=3, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='route',
            name='marker',
            field=models.CharField(max_length=100, verbose_name='Метка'),
        ),
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='route',
            name='rank',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='routephoto',
            name='photo',
            field=models.ImageField(upload_to='media/routes/', verbose_name='Фотография'),
        ),
    ]
