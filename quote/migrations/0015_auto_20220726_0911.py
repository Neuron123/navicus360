# Generated by Django 3.1.13 on 2022-07-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0014_auto_20220726_0900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote_air',
            old_name='quote_owner',
            new_name='quote_serial_no',
        ),
        migrations.RenameField(
            model_name='quote_road',
            old_name='quote_owner',
            new_name='quote_serial_no',
        ),
        migrations.RenameField(
            model_name='quote_sea',
            old_name='quote_owner',
            new_name='quote_serial_no',
        ),
        migrations.AddField(
            model_name='quotetype',
            name='quote_serial_no',
            field=models.CharField(default='000', max_length=30),
        ),
    ]
