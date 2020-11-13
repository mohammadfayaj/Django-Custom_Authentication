from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image
from intl_tel_input.widgets import IntlTelInputWidget
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.ImageField(default='default.jpg', upload_to="profile_pic")

    def __str__(self):
        return f'{self.user.username} Profile'


DIVISION = [

    ('Dhaka', 'Dhaka'),
    ('Chittagong', 'Chittagong'),
    ('Barisal', 'Barisal'),
    ('Khulna', 'Khulna'),
    ('Mymensingh', 'Mymensingh'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Sylhet', 'Sylhet'),
]

DELIVERY = [
    ('H', 'Home'),
    ('O', 'Office')
]


class Address (models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True, help_text='Please Enter Your Valid Phone Number.',)
    house_number = models.CharField(max_length=32, blank=True, null=True, help_text='Your Village Name And House Number')
    division = models.CharField(max_length=15, choices=DIVISION, blank=True, null=True)
    effective_delivery = models.CharField(max_length=30, choices=DELIVERY, blank=True, null=True, default='H')
    city = models.CharField(max_length=30, blank=True, null=True)
    zone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.users.username} Address'
