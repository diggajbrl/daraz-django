# Generated by Django 5.1.4 on 2024-12-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_mens_price_alter_womens_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='womens',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]