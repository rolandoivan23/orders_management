# Generated by Django 3.2.5 on 2021-07-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_vendors'),
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='articles',
            field=models.ManyToManyField(to='articles.Article'),
        ),
    ]