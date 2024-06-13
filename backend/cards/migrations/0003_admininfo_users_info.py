# Generated by Django 4.1.7 on 2024-06-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_gpus_note'),
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
    ]