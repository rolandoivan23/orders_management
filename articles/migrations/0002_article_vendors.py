# Generated by Django 3.2.5 on 2021-07-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='vendors',
            field=models.ManyToManyField(related_name='articles', to='vendors.Vendor'),
        ),
    ]
