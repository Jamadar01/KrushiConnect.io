# Generated by Django 4.2.2 on 2023-11-26 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_sell'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell',
            old_name='sell_descripton',
            new_name='sell_description',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='sell_exp',
        ),
    ]
