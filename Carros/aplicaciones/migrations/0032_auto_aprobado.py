# Generated by Django 3.2.5 on 2022-04-20 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0031_auto_20220419_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='aprobado',
            field=models.BooleanField(default=False),
        ),
    ]
