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

class Employee(models.Model):
    employee_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    address= models.CharField(max_length=100)
    about= models.TextField()
    position= models.CharField(max_length=100, choices=(('Manager','Manager'),('Software Developer','Software Developer'),('Project Leader','Project Leader')))
    company= models.ForeignKey(Company,on_delete=models.CASCADE)

