from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date
import datetime

GENDER_CHOICES = [
    (5,     "Male                 "),
    (-161,  "Female               "),
]
EX_CHOICES = [
    (70,     "0-30 minutes         "),
    (250,    "30-90 minutes        "),
    (600,    "More than 90 minutes "),
]
R_Type = [
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner")
]
R_Pref=[
    ("veg","Vegetarian"),
    ("nonveg", "Non-Vegetarian")
]
class accountmanager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('users must have an email address')
        if not username:
            raise ValueError('users must have an username')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_admin =True
        user.is_staff =True
        user.is_superuser =True
        user.save(using=self._db)
        return user
    
class hcondition(models.Model):
    name= models.CharField(max_length=200)
    def __str__(self):
      return self.name
  
#Changing Django's default user model
class account(AbstractBaseUser):
    username=       models.CharField(max_length=30 , unique=True)
    email=          models.EmailField(verbose_name='email',max_length=30)
    dob=            models.DateField(null=True,default=datetime.date.today())
    height=         models.IntegerField(null=True)
    weight=         models.IntegerField(null=True) 
    extype=         models.IntegerField(null=True, choices=EX_CHOICES)
    gender=         models.IntegerField(null=True, choices=GENDER_CHOICES)
    veg=            models.BooleanField(default=False)
    is_superuser=   models.BooleanField(default=False)
    is_admin=       models.BooleanField(default=False) 
    is_active=      models.BooleanField(default=True)
    is_staff=       models.BooleanField(default=False)
    
    def get_age(self):
        age = datetime.date.today()-self.dob
        return int((age).days/365.25)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = accountmanager()
    
    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
    def get_hcon(self):
        return ",".join([str(p) for p in self.hcondition.all()])
    
    

#Probably not going to use suser 

class suser(models.Model):
    name=           models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    hcon=           models.ManyToManyField(hcondition)

class test(models.Model):
    age=            models.DateField()
    
    def get_age(self):
        agem = datetime.date.today()-self.age
        return int((agem).days/365.25)
    
    
class nutpar(models.Model):
    name=           models.CharField(max_length=200)
    desc=           models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    
    
class recipe(models.Model):
    name=           models.CharField(max_length=200)
    rtype=          models.CharField(max_length=10,null=True, choices=R_Type)
    veg =           models.BooleanField(default=False)
    Detail=         models.CharField(max_length=1000)
    hcon=           models.ManyToManyField(hcondition)
    npr=            models.ManyToManyField(nutpar)
    energy=         models.IntegerField(null=True)
    def __str__(self):
      return self.name 


class history(models.Model):
    suserid =       models.ForeignKey(suser,null=True, on_delete=models.SET_NULL)
      

     
class recipe1(models.Model):
    DishName =      models.CharField(max_length=100)
    MealType =      models.CharField(max_length=100)
    Calories =      models.IntegerField()
    Protein =       models.IntegerField()
    Carbohydrates = models.IntegerField()
    Fat =           models.IntegerField()
    Sugar =         models.IntegerField()
    DietaryFiber =  models.IntegerField()
    VitaminA =      models.IntegerField()
    VitaminC =      models.IntegerField()
    Calcium =       models.IntegerField()
    Iron =          models.IntegerField()
    Potassium =     models.IntegerField()
    GlutenFree =    models.BooleanField()
    Vegetarian =    models.BooleanField()
    Vegan =         models.BooleanField()
    DiabeticFriendly = models.BooleanField()
    LactoseFree =   models.BooleanField()
    NutFree =       models.BooleanField()
    LowCarb =       models.BooleanField()
    LowFat =        models.BooleanField()
    HighFiber =     models.BooleanField()
    LowSodium =     models.BooleanField()
    DairyFree =     models.BooleanField()
    EggFree =       models.BooleanField()
    SoyFree =       models.BooleanField()
    
    desc =          models.CharField(max_length=1000)

    def __str__(self):
        return self.DishName