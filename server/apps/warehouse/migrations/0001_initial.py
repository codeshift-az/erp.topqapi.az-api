# Generated by Django 5.0 on 2024-03-06 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('invoice', models.CharField(blank=True, max_length=255)),
                ('date', models.DateField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='supplier.supplier')),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='warehouse.entry')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse', to='product.product')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
    ]
