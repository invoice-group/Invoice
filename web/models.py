from django.db import models
from web.storage import ImageStorage

class User(models.Model):
   user_id = models.CharField(max_length=30)
   user_password = models.CharField(max_length=50)
   user_phone = models.CharField(max_length=30)
   user_img = models.ImageField(upload_to='user_img')

   class Meta:
      db_table = "User"


class Invoice(models.Model):
   user_id = models.CharField(max_length=30)
   inv_numh = models.CharField(max_length=30)
   inv_numd = models.CharField(max_length=30)
   inv_img = models.ImageField(upload_to='inv_img', storage=ImageStorage())
   inv_money = models.FloatField()
   inv_date = models.CharField(max_length=50)

   class Meta:
      db_table = "Invoice"

class Statistics(models.Model):
   sta_user_id = models.CharField(max_length=30)
   sta_num = models.IntegerField()
   sta_total_money = models.FloatField()
   sta_average_money = models.FloatField()

   class Meta:
      db_table = "Statistics"