# Generated by Django 4.2.7 on 2024-03-12 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_sale_car_sale_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='client',
        ),
        migrations.AddField(
            model_name='sale',
            name='client',
            field=models.OneToOneField(default='default title', on_delete=django.db.models.deletion.CASCADE, related_name='client', to='main.client'),
        ),
    ]
