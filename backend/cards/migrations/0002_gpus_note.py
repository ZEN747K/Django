# Generated by Django 4.1.7 on 2024-06-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpus',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
