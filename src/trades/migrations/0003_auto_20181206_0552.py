# Generated by Django 2.1.3 on 2018-12-06 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0002_auto_20181206_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='ccc_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='trade',
            name='coa_code',
            field=models.CharField(max_length=10),
        ),
    ]
