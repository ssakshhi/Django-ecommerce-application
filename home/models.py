from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
CATEGORY_CHOICES = (
    ('pants','Pants'),
    ('shirts', 'Shirts'),
    ('shoes', 'Shoes'),
    ('jackets', 'Jackets'),
)

SIZE_CHOICES = (
    ('xs', 'XS'),
    ('s', 'S'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('xll', 'XLL'),
)

COLOR_CHOICES = (
    ('red', 'Red'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('black', 'Black'),
    ('yellow', 'Yellow'),
    ('pink', 'Pink'),
    ('brown', 'Brown'),
)

class Product(models.Model):
    name = models.CharField(max_length = 20)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length = 20, choices = CATEGORY_CHOICES)
    price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[
        MinValueValidator(limit_value=0.01),
        MaxValueValidator(limit_value=9999.99),
    ])
    description = models.TextField(max_length = 100)
    size = models.CharField(max_length = 20, choices = SIZE_CHOICES)
    color = models.CharField(max_length = 20, choices = COLOR_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    