# Generated by Django 3.2.5 on 2021-07-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
        ('articles', '0003_article_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='vendors',
            field=models.ManyToManyField(to='vendors.Vendor'),
        ),
    ]
