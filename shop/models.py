from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator, FileExtensionValidator
import uuid


class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Shop(models.Model):
    COLOR_CHOICES= (
        ('RED', 'red'),
        ('BLUE', 'blue'),
        ('GREEN', 'green'),
        ('YELLOW', 'yellow'),
        ('ORANGE', 'orange'),
        ('PURPLE', 'purple'),
        ('PINK', 'pink'),
        ('BLACK', 'black'),
        ('WHITE', 'oq'),
        ('GRAY', 'gray'),
        ('BROWN', 'brown'),
    )
    SIZE_CHOICES = (
        ('XS', 'xs'),
        ('S', 's'),
        ('M', 'm'),
        ('XL', 'xl'),
        ('2XL', '2xl'),
        ('XXL', 'xxl'),
        ('3XL', '3xl'),
        ('4XL', '4xl'),
    )
    PRICE_CHOICES = (
        (5, 5),
        (10, 10),
        (15, 15),
        (20, 20),
        (25, 25),
        (35, 35),
        (50, 50),
        (100, 100),
        (200, 200),
    )
    
    ID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=150)
    short_info = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    discreption = models.TextField(
        validators=[MaxLengthValidator(3000)],
    )
    SKU = models.PositiveIntegerField(
        validators=[MinValueValidator(10000000), MaxValueValidator(100000000)],
    )
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, null=True, blank=True)
    color = models.CharField(max_length=6, choices=COLOR_CHOICES, null=True, blank=True)
    price_choice = models.CharField(max_length=3, choices=PRICE_CHOICES, null=True, blank=True)
    review = models.PositiveIntegerField( validators=[MaxValueValidator(5)], )
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    sale = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
class ProductTags(models.Model):
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.tag_id.name} - {self.product_id.name}'
    
    
class ShopImages(models.Model):
    image = models.ImageField(
        upload_to='shop/image/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png'])
        ], 
    )
    product_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.product_id.name} - image {self.id}'
    
    
class Checkout(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    country = models.CharField(max_length=240)
    address_street = models.CharField(max_length=120)
    address_extra = models.CharField(max_length=360, blank=True, null=True)
    town_city = models.CharField(max_length=120)
    country_state = models.CharField(max_length=240)
    postcode = models.CharField(max_length=120)
    phone = models.CharField(max_length=17)
    email = models.EmailField()
    create_an_account = models.BooleanField(default=False)
    account_password = models.CharField(max_length=128)
    order_notes = models.CharField(max_length=260, blank=True, null=True)
    
    def __str__(self):
        return self.first_name
    
    
class Liked(models.Model):
    author_id = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.author_id.first_name} liked {self.product_id.name}'
    
    
class Cart(models.Model):
    author_id = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    remove = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.author_id.first_name} carted {self.quantity} {self.product_id.name}'


class Employes(models.Model):
    full_name = models.CharField(max_length=150)
    professions = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='employes/image/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png',])
        ],
    )