# Generated by Django 3.0.8 on 2020-07-09 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcwapp', '0007_auto_20200708_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledetails',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcwapp.CustomerInformation'),
        ),
    ]