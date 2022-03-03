from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, first_name, last_name, phone_number, password, is_staff, is_superuser):
        """
        Creates and saves a User with the given email, first name, last name,
        phone number and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not first_name:
            raise ValueError('Users must fill in first name')

        if not last_name:
            raise ValueError('Users must fill in last name')

        if not phone_number:
            raise ValueError('Users must fill in phone number')
        now = timezone.now()
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            last_login=now,
            date_joined=now, 
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            is_staff=is_staff,
            is_superuser=is_superuser, 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, phone_number, password, is_staff, is_superuser):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        return self._create_user(
            email,
            first_name,
            last_name,
            phone_number,
            password,
            False,
            False,
        )

    def create_superuser(self, email, first_name, last_name, phone_number, password, is_staff, is_superuser):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user=self._create_user(
            email,
            first_name,
            last_name,
            phone_number,
            password,
            True,
            True,
        )
        user.save(using=self._db)
        return user

# Roles to assign to users
ROLES = (
        (0, 'boss'),
        (1, 'teacher'),
        (3, 'sales'),
        (4, 'receptionist'),
        (5, 'parent'),
        (6, 'potential user'),
)


class User(AbstractBaseUser, PermissionsMixin):
    """User costum model"""
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=50)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    wechat_id = models.CharField(max_length=30)
    role = models.IntegerField(choices=ROLES, default=6)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number',]

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.id)