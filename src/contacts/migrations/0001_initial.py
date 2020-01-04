# Generated by Django 3.0.2 on 2020-01-03 19:03

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('climbingwall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('climbingwall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='climbingwall.Climbingwall')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('climbingwall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='climbingwall.Climbingwall')),
            ],
            options={
                'verbose_name': 'E-mail',
                'verbose_name_plural': 'E-mails',
            },
        ),
    ]
