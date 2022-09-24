# Generated by Django 4.1.1 on 2022-09-24 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('fullName', models.CharField(max_length=45, verbose_name='Nombre')),
                ('documentType', models.CharField(max_length=50, verbose_name='Tipo de Documento')),
                ('document', models.BigIntegerField(max_length=50, primary_key=True, serialize=False, verbose_name='Documento')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('phone', models.BigIntegerField(max_length=15, verbose_name='phone')),
                ('city', models.CharField(max_length=20, verbose_name='city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paciente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('especialidad', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.TimeField(verbose_name='hora')),
                ('id_Medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Aplication.medicos')),
            ],
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(verbose_name='fecha')),
                ('id_Medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.medicos')),
                ('id_Paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.paciente')),
                ('id_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.horarios')),
            ],
        ),
    ]
