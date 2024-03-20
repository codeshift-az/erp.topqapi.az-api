# Generated by Django 5.0 on 2024-03-19 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factory_products', to='category.category')),
            ],
            options={
                'verbose_name': 'Factory Product',
                'verbose_name_plural': 'Factory Products',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
    ]
