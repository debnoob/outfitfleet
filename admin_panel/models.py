from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=15, blank=True, null=True)
    business_type = models.CharField(max_length=50, choices=[('Retailer', 'Retailer'), ('Wholesaler', 'Wholesaler'), ('Distributor', 'Distributor')])
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    shop_logo = models.ImageField(upload_to='shop_logos/', blank=True, null=True)

    def __str__(self):
        return self.shop_name
    


class Manufacturer(models.Model):
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    product_categories = models.CharField(max_length=255)  # This can be a comma-separated list or a ForeignKey to another model
    logo = models.ImageField(upload_to='manufacturers/logos/', blank=True, null=True)
    password = models.CharField(max_length=255)
    terms_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_code = models.CharField(max_length=50)  # added field for code

    def __str__(self):
        return self.category_name


class SignupUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'signup_user'