# Generated by Django 4.2.2 on 2024-04-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_customerprofile_farmerprofile_myorders_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='sell_by',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='sell',
            name='sell_location',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
