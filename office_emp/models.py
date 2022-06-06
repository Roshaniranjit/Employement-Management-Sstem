from django.db import models

# Create your models here.
class Department(models.Model):
    name =  models.CharField(max_length=50)
    location = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    


class Employee(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    hire_date = models.DateField()
    phone = models.CharField(max_length=10)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name
    