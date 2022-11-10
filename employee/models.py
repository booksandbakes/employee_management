import email
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length = 50, unique = True)

    def __str__(self) -> str:
        return self.dept_name

class Employee(models.Model):
    e_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length= 20)
    email = models.EmailField(unique = True)
    phone_no = models.IntegerField(max_length=10)
    salary = models.IntegerField()
    depart_ment = models.ForeignKey(Department, on_delete = models.CASCADE)
    def __str__(self):
       return self.email



