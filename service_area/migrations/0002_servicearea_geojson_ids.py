# Generated by Django 5.0.6 on 2024-06-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_area', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='servicearea',
            index=models.Index(fields=['geojson'], name='geojson_ids'),
        ),
    ]
