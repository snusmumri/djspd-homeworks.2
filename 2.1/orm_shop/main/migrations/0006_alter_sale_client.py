# Generated by Django 4.2.7 on 2024-03-12 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_sale_client_sale_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='main.client'),
        ),
    ]
