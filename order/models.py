from django.db import models
from django.conf import settings
# from django.core.validators import MinValueValidator, MaxValueValidator
from shop.models import Product
from django.utils import timezone
from accounts.models import UserAddress


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    address = models.ForeignKey(UserAddress, related_name='order_addresses', on_delete=models.SET_NULL, null=True)
    authority = models.CharField(max_length=100, null=True)
    post_cost = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"{self.user} - {self.id}"

    @property
    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all()) + self.post_cost
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return str(self.order.user) + str(self.product)

    def get_cost(self):
        return self.product.get_final_price() * self.quantity
