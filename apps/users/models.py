from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin,AbstractUser
from apps.workspace.models import Workspace
# Create your models here.

class MyUserManager(BaseUserManager):
    def _create_user(self,email,first_name,last_name,password,**extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not first_name:
            raise ValueError('First name is required')
        if not last_name:
            raise ValueError('Last name is required')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,email,first_name,last_name,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,first_name,last_name,password,**extra_fields)

    def create_superuser(self,email,first_name,last_name,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,first_name,last_name,password,**extra_fields)

class UserType(models.Model):
    user_type = models.CharField(max_length=30)

class User(AbstractUser):
    username = models.CharField(max_length=40,unique=True)
    first_name = models.CharField(max_length=42)
    last_name = models.CharField(max_length=43)
    email = models.EmailField()
    phone = models.CharField(max_length=45,blank = True,null=True)
    img_profile = models.ImageField(upload_to='media/img_profile',blank = True,null=True)
    birthdate = models.CharField(max_length=40)
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE,blank = True,null=True)

    REQUIRED_FIELDS = ['first_name','last_name','email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username}'

class UsersWorkspaces(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace,on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)


# class User(AbstractBaseUser,PermissionsMixin):
#     username = models.CharField(max_length=40,unique=True)
#     password = models.CharField(max_length=41)
#     first_name = models.CharField(max_length=42)
#     last_name = models.CharField(max_length=43)
#     email = models.CharField(max_length=44)
#     phone = models.CharField(max_length=45,blank = True,null=True)
#     img_profile = models.ImageField(upload_to='media/img_profile',blank = True,null=True)
#     birthdate = models.CharField(max_length=40)
#     user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     objects = MyUserManager()

#     REQUIRED_FIELDS = ['first_name','last_name','email']
#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return f'{self.username}'