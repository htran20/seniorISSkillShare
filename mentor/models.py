from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
import datetime


DEGREE_CHOICES = (
    ("1", "Bachelor's degree"),
    ("2", "Associate degree"),
    ("3", "Master's degree"),
    ("4", "Doctoral degree"),
)

class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = CountryField(multiple=False, default='US')
    zip = models.CharField(max_length=100, default='00000')
    default = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'

class UserMentorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(null=True)
    email = models.CharField(max_length=100, blank=True)
    # address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=500, default="This is a default text")
    school = models.CharField(max_length=100, default="Default school")
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, default='1')
    major = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)


    def __str__(self):
        return self.user.username

    def get_email(self):
        return self.user.email


class MentorProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField(blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=500, default="This is a default text")
    title = models.CharField(max_length=100, default="This is a default title")
    employer = models.CharField(max_length=200, blank=True)
    school = models.CharField(max_length=100, default="Default school")

    school_start_date = models.DateField(default=datetime.date.today)
    school_end_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(blank=True)
    linkedin = models.URLField(max_length=200,  blank=True)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, default='1')
    major = models.CharField(max_length=100, default="Default major")
    certificate = models.CharField(max_length=300, blank=True)
    skills = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("mentor:detail", kwargs={
            'slug': self.slug
        })

class BookingItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    mentor = models.ForeignKey(MentorProfile, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.mentor.name}"

    def get_total_booking_price(self):
        pass

    def get_total_discount_item_price(self):
        pass

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

# class Item(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.FloatField()
#     discount_price = models.FloatField(blank=True, null=True)
#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
#     label = models.CharField(choices=LABEL_CHOICES, max_length=1)
#     slug = models.SlugField()
#     description = models.TextField()
#     image = models.ImageField()
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse("core:product", kwargs={
#             'slug': self.slug
#         })
#
#     def get_add_to_cart_url(self):
#         return reverse("core:add-to-cart", kwargs={
#             'slug': self.slug
#         })
#
#     def get_remove_from_cart_url(self):
#         return reverse("core:remove-from-cart", kwargs={
#             'slug': self.slug
#         })