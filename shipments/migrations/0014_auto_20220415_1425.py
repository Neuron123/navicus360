# Generated by Django 3.1.13 on 2022-04-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0013_alter_roadfreightship_shippingstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airfreightship',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customclearance',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='freightforwarding',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='roadfreightship',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='seafreightship',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
