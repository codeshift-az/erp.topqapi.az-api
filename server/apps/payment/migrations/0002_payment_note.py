# Generated by Django 5.1 on 2024-10-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
