# Generated by Django 4.1.4 on 2023-01-28 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0002_alter_order_options_order_authority_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=10)),
                ('address_text', models.CharField(max_length=100)),
                ('name_of_transferee', models.CharField(max_length=20)),
                ('phone_of_transferee', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('post_tracking_code', models.CharField(max_length=24, null=True)),
                ('is_post_delivered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('authority', models.CharField(max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_pack', to='order.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_packs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
