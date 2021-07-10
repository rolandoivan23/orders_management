# Generated by Django 3.2.5 on 2021-07-10 14:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_vendors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=12, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
