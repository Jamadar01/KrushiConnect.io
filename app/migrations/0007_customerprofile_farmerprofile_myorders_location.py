# Generated by Django 4.2.2 on 2024-04-30 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_sell_descripton_sell_sell_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('location', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('location', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='myorders',
            name='location',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
