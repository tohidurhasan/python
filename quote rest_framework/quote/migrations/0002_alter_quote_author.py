# Generated by Django 5.1.5 on 2025-01-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
