# Generated by Django 4.1.7 on 2024-06-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_admininfo_users_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('graphics_card_id', models.PositiveIntegerField()),
            ],
        ),
    ]
