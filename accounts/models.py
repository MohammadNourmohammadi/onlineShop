from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import MyUserManager


class MyUser(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "A user with that email already exists.",
        },
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(
        max_length=15, unique=True, error_messages={
            'unique': "A user with that phone number already exists."
        })

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return self.email


class UserAddress(models.Model):
    name = models.CharField(max_length=30, default="خانه")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='address')
    zip_code = models.CharField(max_length=10)
    address_text = models.CharField(max_length=100)
    name_of_transferee = models.CharField(max_length=20)
    phone_of_transferee = models.CharField(max_length=15)
    state = models.CharField(max_length=30, default='تهران')
    city = models.CharField(max_length=30, default='تهران')

    def __str__(self):
        return self.name
