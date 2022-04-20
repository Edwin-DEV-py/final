# Generated by Django 3.2.5 on 2022-04-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0030_direccion_fin_direccion_inicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion_inicio', models.CharField(choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11)),
                ('cc_ini', models.CharField(max_length=10)),
                ('numero_ini', models.CharField(max_length=10)),
                ('extra_ini', models.CharField(max_length=100)),
                ('direccion_fin', models.CharField(choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11)),
                ('cc_fin', models.CharField(max_length=10)),
                ('numero_fin', models.CharField(max_length=10)),
                ('extra_fin', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Direccion_fin',
        ),
        migrations.DeleteModel(
            name='Direccion_inicio',
        ),
    ]
