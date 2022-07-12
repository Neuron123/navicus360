# Generated by Django 3.1.13 on 2022-06-24 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0027_auto_20220605_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='cargo_weight',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='other_vas',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='truck_size',
            field=models.CharField(blank=True, choices=[('van', 'Van'), ('3T', '3T Truck'), ('5T', '5T Truck'), ('7T', '7T Truck'), ('10T', '10T Truck'), ('15T', '15T Truck'), ('28T', '28T Truck')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='collection_address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='country_origin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='incoterms',
            field=models.CharField(blank=True, choices=[('EX', 'EX Works'), ('FOB', 'FOB'), ('CRF', 'CRF'), ('DAP', 'DAP'), ('OTHER', 'Other')], default='EX', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='special_instructions',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
