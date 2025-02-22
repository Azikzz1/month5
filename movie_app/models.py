from django.db import models
import random
import string


class Director(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    objects = None
    text = models.TextField()
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    stars = models.IntegerField(default=1)

    def __str__(self):
        return f'Review for {self.movie.title}'


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=6, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def generate_confirmation_code(self):
        self.confirmation_code = ''.join(random.choices(string.digits, k=6))
        self.save()

    def __str__(self):
        return self.email
