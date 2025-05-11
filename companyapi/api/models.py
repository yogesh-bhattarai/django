from django.db import models

# Create your models here.
class Company(models.Model):
    #schoices=(('IT','IT'),('Non IT','Non IT'),('Mobile Phones','Mobile Phones'))
    company_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    about= models.TextField()
    types= models.CharField(max_length=100, choices=(('IT','IT'),('Non IT','Non IT'),('Mobile Phones','Mobile Phones')))
    active= models.BooleanField(default=True)

