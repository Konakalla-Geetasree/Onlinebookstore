# Generated by Django 3.1 on 2024-04-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20240420_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
