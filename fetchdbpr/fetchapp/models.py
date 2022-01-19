from django.db import models

# Create your models here.

class fetchingdb(models.Model):
    sl_no= models.IntegerField()
    iname= models.CharField(max_length=100)
    iquantity= models.IntegerField()
    price= models.FloatField()
    
