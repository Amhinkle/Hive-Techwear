# Generated by Django 3.2.7 on 2022-04-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity'),
        ),
    ]