# Generated by Django 5.2.1 on 2025-06-18 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllableconnect', '0006_rename_sounds_syllablebank_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllablebank',
            name='audio_json',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
