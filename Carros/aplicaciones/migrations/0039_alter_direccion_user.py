# Generated by Django 3.2.5 on 2022-04-27 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0038_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to='aplicaciones.autos'),
        ),
    ]