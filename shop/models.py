from django.db import models
from django.urls import reverse


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True,
                                     blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('shop:category_detail', args={self.slug})


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    image = models.ImageField(upload_to='static/shop/images')
    description = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    country_made = models.CharField(max_length=20)
    exp_date = models.DateField()
    pro_date = models.DateField()

    class Meta:
        ordering = ('?',)

    def __str__(self):
        return self.name

    def get_final_price(self):
        return int(self.price * (100 - self.discount) // 100)

    def get_absolut_url(self):
        return reverse('shop:product_detail', args={self.slug, })


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='static/shop/images')
