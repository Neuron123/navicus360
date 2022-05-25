# Generated by Django 3.1.13 on 2022-05-16 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0009_auto_20220511_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('supervisor', 'Supervisor'), ('completed', 'Completed'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
