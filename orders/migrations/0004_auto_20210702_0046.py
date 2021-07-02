# Generated by Django 3.2.5 on 2021-07-02 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210702_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailorderassociatedcompany',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='associated_company_details', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='detailorderbranchoffice',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='branch_office_details', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='detailorderdistributioncenter',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='distribution_center_details', to='orders.order'),
        ),
    ]
