# Generated by Django 3.2.5 on 2021-08-02 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eventos', '0001_initial'),
        ('perfil_empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.eventomodel')),
                ('user', models.ManyToManyField(to='perfil_empresa.PerfilEmpresa')),
            ],
        ),
    ]
