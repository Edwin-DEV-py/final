# Generated by Django 3.2.5 on 2022-04-14 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0004_auto_20220413_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cedula',
            field=models.CharField(max_length=10, verbose_name='cedula'),
        ),
        migrations.AlterField(
            model_name='user',
            name='certificado',
            field=models.ImageField(blank=True, null=True, upload_to='certificados'),
        ),
        migrations.AlterField(
            model_name='user',
            name='direccion',
            field=models.CharField(max_length=150, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(upload_to='Fotografias'),
        ),
    ]
