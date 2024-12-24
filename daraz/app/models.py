from django.db import models

class Mens (models.Model) :
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length = 100)
    price = models.CharField(max_length = 10)

    def __str__ (self) :
        return self.description
    

class Womens(models.Model):

    CATEGORIES_CHOICE = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Baby', 'Baby'),
        ('Cap', 'Cap'),
        ('Shoe', 'Shoe'),
    ]

    CURRENCY_SIGN = [
        ('$', 'USD'),
        ('€', 'EURO'),
        ('₹', 'INR'),
        ('रु', 'NRP'),
    ]
    
    image = models.ImageField(upload_to='images/')
    img_alt = models.CharField(max_length=300)
    description = models.CharField(max_length=100)
    categories = models.CharField(max_length = 5, choices= CATEGORIES_CHOICE)
    currency = models.CharField(max_length=5, choices=CURRENCY_SIGN, default='$')
    price = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.img_alt} - {self.categories}'
    
class Product(models.Model):

    CATEGORIES_CHOICE = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Baby', 'Baby'),
        ('Cap', 'Cap'),
        ('Shoe', 'Shoe'),
    ]

    CURRENCY_SIGN = [
        ('$', 'USD'),
        ('€', 'EURO'),
        ('₹', 'INR'),
        ('रु', 'NRP'),
    ]

    SIZE_CHOICE = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
    ]
    
    image = models.ImageField(upload_to='images/')
    img_alt = models.CharField(max_length=300)
    description = models.CharField(max_length=100)
    size = models.CharField(max_length = 5, choices = SIZE_CHOICE)
    categories = models.CharField(max_length = 5, choices= CATEGORIES_CHOICE)
    currency = models.CharField(max_length=5, choices=CURRENCY_SIGN, default='$')
    price = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.img_alt} - {self.categories}'