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


class Homee(models.Model):
  id=models.AutoField(primary_key=True)
  title=models.TextField(null=False,blank=False)
  description=models.TextField(null=True,blank=True)


class About_me(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=100, null=False,blank=False)
  age=models.IntegerField(null=False,blank=False)
  home=models.CharField(max_length=100, null=False,blank=False)
  current_loacation=models.CharField(max_length=100, null=False,blank=False)
  phone=models.CharField(max_length=20, null=False,blank=False)
  description=models.TextField(null=True,blank=True)

class Service(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=100, null=False,blank=False)
  icon=models.CharField(max_length=100, null=False,blank=False)
  description=models.TextField(null=True,blank=True)

class Education(models.Model):
  id=models.AutoField(primary_key=True)
  title=models.CharField(max_length=100, null=False,blank=False)
  class_name=models.CharField(max_length=200, null=False,blank=False)
  time=models.CharField(max_length=100, null=False,blank=False)
  location=models.CharField(max_length=200, null=False,blank=False)
  description=models.TextField(null=True,blank=True)

class Contact (models.Model):
  id=models.AutoField(primary_key=True)
  icon=models.CharField(max_length=100, null=False,blank=False)
  link1=models.CharField(max_length=100, null=False,blank=False)
  link2=models.CharField(max_length=100, null=False,blank=False)
  

class Achievement(models.Model):
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



