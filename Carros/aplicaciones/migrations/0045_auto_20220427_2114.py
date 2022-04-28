# Generated by Django 3.2.5 on 2022-04-28 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicaciones', '0044_auto_20220427_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direccion',
            name='disliked',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Elegir', 'Elegir'), ('Deselegir', 'Deselegir')], default='Like', max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicaciones.direccion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
