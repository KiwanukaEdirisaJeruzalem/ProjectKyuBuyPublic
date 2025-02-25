# Generated by Django 4.2.16 on 2024-09-27 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('retailerrating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('technicianrating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('retailer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RetailsAndTechs.retailer')),
                ('technician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RetailsAndTechs.technician')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
