from django.db import models

class ProductModel(models.Model):
    pname =  models.CharField(max_length=100, default='')
    pprice = models.IntegerField(default=0)
    pimages = models.CharField(max_length=100, default='')
    pdescription = models.TextField(blank=True, default='')
    def __str__(self):
        return self.pname
        
class OrdersModel(models.Model):
    subtotal = models.IntegerField(default=0)
    shipping = models.IntegerField(default=0)
    grandtotal = models.IntegerField(default=0)
    customname =  models.CharField(max_length=100, default='')
    customemail =  models.CharField(max_length=100, default='')
    customaddress =  models.CharField(max_length=100, default='')
    customphone =  models.CharField(max_length=100, default='')
    paytype =  models.CharField(max_length=50, default='')
    def __str__(self):
        return self.customname
     
class DetailModel(models.Model):
    dorder = models.ForeignKey('OrdersModel', on_delete=models.CASCADE)
    pname = models.CharField(max_length=100, default='')
    unitprice = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    dtotal = models.IntegerField(default=0)
    def __str__(self):
        return self.pname

class BoardUnit(models.Model):
    bname = models.CharField(max_length=20, null=False)
    bgender = models.CharField(max_length=2, default='m', null=False)
    bsubject = models.CharField(max_length=100, null=False)
    btime = models.DateTimeField(auto_now=True)
    bmail = models.EmailField(max_length=100, blank=True, default='')
    bweb = models.CharField(max_length=200, blank=True, default='')
    bcontent = models.TextField(null=False)
    bresponse = models.TextField(blank=True, default='')
    
    def __str__(self):
        return self.bsubject