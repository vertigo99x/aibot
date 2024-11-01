from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
import uuid 

from django.conf import settings

HOST = settings.HOST


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="profiles", null=True, blank=True)
    username = None
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []  
    objects = CustomUserManager()

    def get_profile_image(self):
        if self.image:
            return HOST + self.image.url
        else:
            return "https://pixabay.com/vectors/blank-profile-picture-mystery-man-973460"