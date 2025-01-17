# Generated by Django 4.2.11 on 2025-01-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('brand_name', models.CharField(max_length=100)),
                ('size', models.CharField(blank=True, max_length=50, null=True)),
                ('condition', models.CharField(max_length=50)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('second_hand_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_urls', models.JSONField()),
                ('authenticity_docs', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('sold', 'Sold')], default='active', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
