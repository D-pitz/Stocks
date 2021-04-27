from django.db import models

# class Stock(models.Model):
#     #User has many to many relationship with Stock
#     symbol = models.CharField(max_length=10)
#     user = models.ManyToManyField(User, related_name= 'stocks')
#     #user_stocks
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class User_stock(models.Model):
#     #User has on to many relationship with User_Stock
#     symbol = models.CharField(max_length=10)
#     date_purchased = models.DateField()
#     purchase_price = models.IntegerField()
#     stocks = models.ForeignKey(Stock, related_name='user_stocks', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name='user_stocks', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

