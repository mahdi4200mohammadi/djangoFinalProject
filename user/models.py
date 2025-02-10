from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,password=None,**extra_fields):
        if not first_name:
            raise ValueError("First name is required")
        if not last_name:
            raise ValueError("Last name is required")
        if not email:
            raise ValueError("Email field is required")
        if not password:
            raise ValueError("Password field is required")

        email=self.normalize_email(email)
        user=self.model(first_name=first_name,last_name=last_name,email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,first_name,last_name,email,username,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("super user should have is_staff true")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("super user should have is_superuser true")
        return self.create_user(first_name,last_name,email,username,password,**extra_fields)
 

class User(AbstractUser):
    email=models.EmailField(unique=True)
    birthday=models.DateField(null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    objects=UserManager()


    groups = models.ManyToManyField(Group, related_name="custom_user_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions")


    def __str__(self):
        return self.email


class Profile(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female')
    ]
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    image=models.ImageField(upload_to='profile_images/.')
    bio=models.TextField()
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)