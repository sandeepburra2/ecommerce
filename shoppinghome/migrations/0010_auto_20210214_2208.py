# Generated by Django 3.1.5 on 2021-02-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinghome', '0009_auto_20210128_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.CharField(max_length=500),
        ),
    ]
