# Generated by Django 4.1.4 on 2023-05-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_deliverypack_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverypack',
            name='ref_id',
            field=models.CharField(max_length=30),
        ),
    ]
