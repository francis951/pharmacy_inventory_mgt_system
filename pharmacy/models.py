from django.db import models
from django.utils.timezone import *
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    #this method gives a human readible name for the interface of the class which is our our category
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    item_name = models.CharField(max_length = 50, null = True, blank = True)
    total_quantity = models.IntegerField(default = 0, null=True, blank = True)
    issued_quantity = models.IntegerField(default = 0, null = True, blank = True)
    recieved_quantity = models.IntegerField(default = 0, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)
    manufacture = models.CharField(max_length = 50, null = True, blank = True)
    brand = models.CharField(max_length = 50, null = True, blank = True)
    
    def __str__(self):
        return self.item_name

class Sale(models.Model):
        item = models.ForeignKey(Product, on_delete = models.CASCADE)
        quantity = models.IntegerField(default=0, null=False, blank=True)
        amount_received = models.IntegerField(default=0, null=False, blank=True)
        issue_to = models.CharField(max_length = 50, null = True, blank = True)
        unit_price = models.IntegerField(default = 0, null = False, blank = True)
        # user = models.ForeignKey(User, on_delete= models.CASCADE)
        date = models.DateField(auto_now_add= False)
        #calculating total
        def get_total(self):
            total = self.quantity * self.unit_price
            return int(total)
        #calculating change
        def get_change(self):
            change = self.get_total() - self.amount_received
            return abs(int(change))
        
        def get_vat(self):
            vat =(self.get_total * 0.18) * 100
            return vat
        #Adding fields
        def __str__(self):
            return self.item.item_name