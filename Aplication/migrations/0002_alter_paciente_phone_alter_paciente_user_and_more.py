# Generated by Django 4.1.1 on 2022-09-24 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='document',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256, verbose_name='Password'),
        ),
    ]
