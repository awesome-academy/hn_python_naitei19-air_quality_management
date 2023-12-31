# Generated by Django 3.2.20 on 2023-09-20 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pollutant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SO2', models.DecimalField(decimal_places=4, max_digits=18)),
                ('O3', models.DecimalField(decimal_places=4, max_digits=18)),
                ('PM2_5', models.DecimalField(decimal_places=4, max_digits=18)),
                ('PM10', models.DecimalField(decimal_places=4, max_digits=18)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='profile_images')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AirQualityData',
            fields=[
                ('data_id', models.UUIDField(default=uuid.uuid4, help_text='Unique Id for this data', primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=200)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('air_quality_index', models.DecimalField(decimal_places=4, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pol_level', models.CharField(blank=True, max_length=200)),
                ('provider', models.CharField(max_length=200)),
                ('pollutant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.pollutant')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
