# Generated by Django 3.2.5 on 2022-04-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0007_auto_20220413_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cedula',
            field=models.CharField(max_length=10, null=True, verbose_name='cedula'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telefono',
            field=models.CharField(max_length=10, null=True, verbose_name='telefono'),
        ),
    ]
