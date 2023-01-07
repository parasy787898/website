from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=100,null=False,blank=False)
  percentage=models.IntegerField(null=False,blank=False)

class Exp(models.Model):
  id=  id=models.AutoField(primary_key=True)
  profile=models.CharField(max_length=150,null=True,blank=True)
  employer=models.CharField(max_length=100,null=True,blank=True)
  time=models.CharField(max_length=30,null=True,blank=True)
  location=models.TextField(null=True,blank=True)
  company_description=models.TextField(null=True,blank=True)
  job_description=models.TextField(null=True,blank=True)



class Client(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=100,null=False,blank=False)
  position=models.CharField(max_length=100,null=False,blank=False)
  description=models.TextField(max_length=100,null=False,blank=False)

class Portfolio(models.Model):
  id=models.AutoField(primary_key=True)
  title=models.CharField(max_length=100,null=False,blank=False)
  description=models.TextField(max_length=100,null=False,blank=False)
  image=models.ImageField(null=True,blank=True)
  group=models.CharField(max_length=30,null=False,blank=False)

  @property
  def imageURL(self):
    try:
      url= self.image.url 
    except:
      url=''
    return url

class Certificate(models.Model):
  id=models.AutoField(primary_key=True)
  title=models.CharField(max_length=100,null=False,blank=False)
  description=models.TextField(max_length=100,null=True,blank=True)
  image=models.ImageField(null=True,blank=True)
  group=models.CharField(max_length=30,null=False,blank=False)

  @property
  def imageURL(self):
    try:
      url= self.image.url 
    except:
      url=''
    return url



