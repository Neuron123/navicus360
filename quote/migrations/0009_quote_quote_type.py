# Generated by Django 3.1.13 on 2022-07-24 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0008_quote_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='quote_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quote.quotetype'),
            preserve_default=False,
        ),
    ]
