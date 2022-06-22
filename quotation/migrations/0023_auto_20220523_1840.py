# Generated by Django 3.1.13 on 2022-05-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0022_auto_20220523_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]