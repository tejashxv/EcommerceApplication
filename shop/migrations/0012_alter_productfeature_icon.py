# Generated by Django 5.1.7 on 2025-03-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_productfeature_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeature',
            name='icon',
            field=models.CharField(choices=[('fa fa-check text-green-500', 'Check Mark'), ('fa fa-times text-red-500', 'Cross/X Mark'), ('fa fa-star text-yellow-500', 'Star'), ('fa fa-heart text-red-700', 'Heart'), ('fa fa-bolt text-yellow-400', 'Bolt'), ('fa fa-leaf text-green-600', 'Leaf'), ('fa fa-shield text-blue-500', 'Shield'), ('fa fa-truck text-indigo-500', 'Truck'), ('fa fa-lock text-gray-600', 'Lock'), ('fa fa-battery-full text-green-600', 'Battery')], default='fa fa-check', max_length=50),
        ),
    ]
