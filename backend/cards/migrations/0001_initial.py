# Generated by Django 4.1.7 on 2024-06-21 04:47

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
            name='AdminInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=10)),
                ('time_login', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GPUs',
            fields=[
                ('products_id', models.AutoField(primary_key=True, serialize=False)),
                ('GPU_id', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('slot', models.CharField(max_length=255)),
                ('chipset', models.CharField(max_length=255)),
                ('series', models.CharField(max_length=255)),
                ('gpu_model', models.CharField(max_length=255)),
                ('gpu_speed_oc', models.PositiveIntegerField()),
                ('gpu_speed_gaming', models.PositiveIntegerField()),
                ('memory_speed', models.PositiveIntegerField()),
                ('memory_size', models.PositiveIntegerField()),
                ('memory_type', models.CharField(max_length=255)),
                ('cuda_cores', models.PositiveIntegerField()),
                ('length', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('max_resolution', models.CharField(max_length=255)),
                ('directx_support', models.CharField(max_length=255)),
                ('crossfire_sli_support', models.CharField(max_length=255)),
                ('dvi_port', models.PositiveIntegerField()),
                ('hdmi_port', models.PositiveIntegerField()),
                ('display_port', models.PositiveIntegerField()),
                ('option_port', models.CharField(max_length=255)),
                ('power_consumption', models.CharField(max_length=255)),
                ('power_supply_requirement', models.PositiveIntegerField()),
                ('power_connectors', models.CharField(max_length=255)),
                ('warranty_years', models.PositiveIntegerField()),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='users_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_num', models.CharField(max_length=255)),
                ('store_name', models.CharField(max_length=255)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.gpus')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='store_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
