# Generated by Django 4.2.2 on 2023-11-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_medicines_delete_sell'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_category', models.CharField(max_length=250)),
                ('sell_name', models.CharField(max_length=250)),
                ('sell_image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('sell_price', models.IntegerField()),
                ('sell_descripton', models.TextField()),
                ('sell_exp', models.DateField()),
            ],
        ),
    ]
