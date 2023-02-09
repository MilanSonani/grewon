from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    objects = CustomUserManager()


class Events(models.Model):
    title = models.CharField(max_length=255)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class EventUser(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)