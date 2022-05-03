# Generated by Django 3.2.5 on 2022-04-30 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0047_auto_20220428_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='cc_2',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='cc_3',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='cc_4',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='direccion_2',
            field=models.CharField(blank=True, choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='direccion_3',
            field=models.CharField(blank=True, choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='direccion_4',
            field=models.CharField(blank=True, choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='direccion_fin',
            field=models.CharField(blank=True, choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='extra_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='extra_3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='extra_4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='numero_2',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='numero_3',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='numero_4',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]