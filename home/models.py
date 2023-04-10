from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length= 500, unique = True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length= 200)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    slug = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length= 500, blank = True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length= 200)
    image = models.ImageField(upload_to ="media")
    description = models.TextField()
    ranks = models.IntegerField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length= 500)
    image = models.ImageField(upload_to= 'media')
    slug = models.CharField(max_length = 500, unique= True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length= 300)
    email = models.EmailField(max_length= 300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Information(models.Model):
    address= models.CharField(max_length = 400)
    phone = models.CharField(max_length= 50)
    email = models.EmailField(max_length = 500)

    def __str__(self):
        return self.address1


STATUS = (('Active', 'Active'), ('Inactive', 'Inactive'))
LABELS = (('new', 'new'), ('hot', 'hot'), ('sale', 'sale'), ('', 'default'))


class Product(models.Model):
    name = models.CharField(max_length = 300)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to = 'media')
    description = RichTextField()
    specification = RichTextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    slug = models.CharField(max_length = 500, unique = True)
    status = models.CharField(choices= STATUS, max_length= 50)
    labels = models.CharField(choices = LABELS, max_length = 50)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    name = models.CharField(max_length= 300)
    image = models.ImageField(upload_to= 'media')
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    name = models.CharField(max_length= 300)
    email = models.EmailField(max_length= 300)
    date = models.DateTimeField(auto_now_add= True)
    star = models.IntegerField()
    comment = models.TextField()
    slug = models.CharField(max_length = 500)

    def __str__(self):
        return self.name


class Cart(models.Model):
    username = models.CharField(max_length = 300)
    slug = models.CharField(max_length= 300)
    quantity = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add= True)
    checkout = models.BooleanField(default = False)
    items = models.ForeignKey(Product, on_delete = models.CASCADE)

    def __str__(self):
        return self.username