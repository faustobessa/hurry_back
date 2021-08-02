# Generated by Django 3.2.5 on 2021-08-02 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('spotfy', models.URLField(blank=True, null=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.eventomodel')),
            ],
        ),
        migrations.CreateModel(
            name='EventoArtistaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='artistas.artistamodel')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.eventomodel')),
            ],
        ),
    ]
