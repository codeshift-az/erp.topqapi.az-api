# Generated by Django 5.0 on 2024-03-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercartitem',
            name='size',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
