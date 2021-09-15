from django.db import models

# Create your models here.
class enquqry_form(models.Model):
    name=models.CharField(max_length=300,unique=True)
    email=models.EmailField()
    class_name=models.CharField(max_length=300)
    phone_number=models.IntegerField()
    start_date=models.IntegerField()

class student(models.Model):
    name=models.ForeignKey(enquqry_form,on_delete=models.CASCADE)
    email=models.EmailField()
    phone_number=models.IntegerField()
    course_name=models.CharField(max_length=300)
    class_fee=models.IntegerField()
    joining_date=models.IntegerField()
    parent_phno=models.IntegerField()

class course(models.Model):
    name=models.ForeignKey(enquqry_form,on_delete=models.CASCADE)
    duriation=models.IntegerField()
    fee=models.IntegerField()
    trainer_name=models.CharField(max_length=300)

class trainer(models.Model):
    name=models.ForeignKey(course,on_delete=models.CASCADE)
    phone_number=models.IntegerField()
    total_fee=models.IntegerField()
    joining_date=models.IntegerField()