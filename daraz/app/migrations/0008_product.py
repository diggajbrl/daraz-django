# Generated by Django 5.1.4 on 2024-12-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_womens_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('img_alt', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], max_length=5)),
                ('categories', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Baby', 'Baby'), ('Cap', 'Cap'), ('Shoe', 'Shoe')], max_length=5)),
                ('currency', models.CharField(choices=[('$', 'USD'), ('€', 'EURO'), ('₹', 'INR'), ('रु', 'NRP')], default='$', max_length=5)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
