# Generated by Django 3.0.8 on 2020-07-09 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcwapp', '0008_auto_20200709_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinformation',
            name='customer_id',
        ),
    ]
