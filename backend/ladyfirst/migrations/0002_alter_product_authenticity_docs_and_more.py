# Generated by Django 5.0.6 on 2025-01-29 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladyfirst', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='authenticity_docs',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_urls',
            field=models.URLField(max_length=255),
        ),
    ]
