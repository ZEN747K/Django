# Generated by Django 4.1.7 on 2024-06-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_store_graphics_card_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='products',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
