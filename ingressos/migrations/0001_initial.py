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
            name='IngressoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('lote', models.SmallIntegerField()),
                ('quantidade', models.IntegerField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.eventomodel')),
            ],
        ),
    ]
