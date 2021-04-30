from django.db import models
from login_app.models import User

# class Stock(models.Model):
#     symbol = models.CharField(max_length=10)
#     company_name = models.CharField()
#     current_price = models.DecimalField()
#     date_purchased = models.DateField()
#     # twenty_four = models.DecimalField()
#     # one_week = models.DecimalField()
#     # one_month = models.DecimalField()
#     # one_year = models.DecimalField()
#     follow = models.ManyToManyField(User, related_name='follows')
#     user = models.ManyToManyField(User, through='Buy_order')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#       def current_value():
#           current_value = current_price * shares
#           return current_value

# class Buy_order(models.Model):
#     symbol = models.CharField(max_length=50)
#     price_purchased = models.IntegerField()
#     current_value = models.DecimalField(current_value())
#  or current value = purchased price and is subtracted from
#     shares = models.IntegerField()
#     date_purchased = models.DateField()
#     owned = models.BooleanField(default=True)
#     stock = models.ForeignKey(Stock, related_name='stock_owned', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name='user_owned', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)  

# class Sell_order(models.Model):
#     symbol = models.CharField(max_length=50)
#     price_sold = models.DecimalField()
#     shares = models.IntegerField()
#     date_sold = models.DateField()
#     stock = models.ForeignKey(Stock, related_name='stock_sold', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name='user_sold', on_delete=models.CASCADE)
#     buy = models.ForeignKey(Buy_order, related_name='sold', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

