# Generated by Django 3.1.13 on 2022-07-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0022_quote_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote_app',
            name='country_destination',
            field=models.CharField(default='0', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote_app',
            name='country_origin',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
