from django.db import models

# Create your models here.

class customerModel(models.Model):
    c=[('M','Male'),('F','Female')]
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    mail=models.EmailField(max_length=250)
    mobile=models.CharField(max_length=10)
    Gender=models.CharField(choices=c,max_length=100)
    status=models.IntegerField(default=1,editable=False)
    class Meta:
        db_table='customer'
class dogModel(models.Model):
     c=[('M','Male'),('F','Female')]
     d=[('W','White'),('B','Black'),('G','Gold'),('GR','Grey')]

     id=models.AutoField(primary_key=True)
     breedname=models.CharField(max_length=250)
     color=models.CharField(choices=d,max_length=100)
     Gender=models.CharField(choices=c,max_length=100)
     available=models.IntegerField(default=1,editable=False)
     class Meta:
         db_table='Dogs'