from django.db import models

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures')

   class Meta:
      db_table = "profile"

class User(models.Model):
   user_id = models.CharField(max_length=30)
   user_name = models.CharField(max_length=50)
   user_password = models.CharField(max_length=50)
   user_phone = models.IntegerField()
   user_img = models.ImageField(upload_to='user_img')
   user_admin = models.BooleanField

   class Meta:
      db_table = "User"


class Invoice(models.Model):
   user_id = models.CharField(max_length=30)
   inv_numh = models.CharField(max_length=30)
   inv_numd = models.CharField(max_length=30)
   inv_img = models.ImageField(upload_to='invoice_img')
   inv_money = models.FloatField()
   inv_date = models.DateField()
   inv_class = models.CharField(max_length=30)

   class Meta:
      db_table = "Invoice"

class Statistics(models.Model):
   sta_user_id = models.CharField(max_length=30)
   sta_num = models.IntegerField()
   sta_total_money = models.FloatField()
   sta_average_money = models.FloatField()
   class Meta:
      db_table = "Statistics"