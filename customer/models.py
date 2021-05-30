from django.db import models

# Create your models here.

class Account(models.Model):
    user_name = models.CharField(max_length=100)
    pass_word = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    role = models.CharField(max_length=100, default='ROLE_USER')
    def __str__(self):
        return self.user_name
       
class Fullname(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def _str_(self):
        return self.first_name
    

class Address(models.Model):
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    villate = models.CharField(max_length=100)
    number_house = models.CharField(max_length=100)
    def __str__(self):
        return self.city + self.district + self.villate + self.number_house

class User(models.Model):
    date_of_birth = models.DateField()
    number_phone = models.CharField(default='',max_length=100)
    email = models.EmailField(default='')
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    full_name = models.ForeignKey(Fullname,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    def __str__(self):
        return self.account.user_name


