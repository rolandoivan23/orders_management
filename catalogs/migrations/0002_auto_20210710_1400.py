# Generated by Django 3.2.5 on 2021-07-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertype',
            name='key',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ordertype',
            name='key',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
