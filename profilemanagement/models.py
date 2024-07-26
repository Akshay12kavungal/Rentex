from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

from renting.models import Camera
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    transaction_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Wallet"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    item = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now() + timedelta(days=1))
    rental_duration_days = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        # Calculate rental duration
        self.rental_duration_days = (self.end_date - self.start_date).days
        # Calculate total price assuming price per day
        self.total_price = self.quantity * self.rental_duration_days * self.item.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order by {self.user.username} on {self.order_date}"
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    item = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item} in {self.user.username}'s Cart"

    @property
    def total_price(self):
        if hasattr(self.item, 'price'):
            return self.quantity * self.item.price
        return 0
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name
