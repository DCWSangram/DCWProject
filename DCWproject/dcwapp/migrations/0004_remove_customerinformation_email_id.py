# Generated by Django 3.0.8 on 2020-07-08 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcwapp', '0003_customerinformation_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinformation',
            name='email_id',
        ),
    ]