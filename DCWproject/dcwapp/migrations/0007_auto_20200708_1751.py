# Generated by Django 3.0.8 on 2020-07-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcwapp', '0006_auto_20200708_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinformation',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]