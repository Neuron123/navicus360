# Generated by Django 3.1.13 on 2022-05-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0018_auto_20220522_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_quotation',
            name='sub_total_duties',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff_quotation',
            name='sub_total_taxes',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]