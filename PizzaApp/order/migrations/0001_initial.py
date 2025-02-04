# Generated by Django 5.1.4 on 2025-01-06 10:38

import django.db.models.deletion
import order.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizza', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(blank=True, default=order.models.generate_uuid, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Confirmed', 'Confirmed'), ('On route', 'On route'), ('Delivered', 'Received'), ('Received', 'Received')], default='Picked-up', max_length=30, null=True)),
                ('pizza', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pizza.pizza')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
