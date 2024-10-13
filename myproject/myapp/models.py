from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class branch(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    branch_name = models.CharField(max_length=225,blank=True, null=True)
    phone = models.CharField(max_length=225,blank=True, null=True)
    address = models.CharField(max_length=225,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branch_name


class branchstaff(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE, blank=True, null=True)
    active_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class category(models.Model):
    branch = models.ForeignKey(branch, on_delete=models.CASCADE, blank=True, null=True)
    usr = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

class product(models.Model):
    branch = models.ForeignKey(branch, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, blank=True, null=True)
    saleprice = models.PositiveIntegerField(default=0)
    purchaseprice = models.PositiveIntegerField(default=0)
    stockbalance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





class Cart(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE, blank=True, null=True)
    total = models.PositiveIntegerField(default=0)
    tax = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    subtotal = models.PositiveIntegerField(default=0)
    remain_balance = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Cart : "+ str(self.cart.id)+ "CartProduct : " + str(self.id)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE, blank=True, null=True)
    customername = models.CharField(max_length=255,null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255,null=True, blank=True)
    orderstatus = models.PositiveIntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)