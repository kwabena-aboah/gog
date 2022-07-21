from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from .validators import validate_image_extension
from report.models import District, Region

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)

        user = self.model(
            email=email,
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
    username = None
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True,)
    name_on_id = models.CharField(max_length=100, null=True, blank=True)
    national_id_number = models.CharField(max_length=8, null=True, blank=True)
    digital_address = models.CharField(max_length=8, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    district_code = models.CharField(max_length=8, null=True, blank=True)
    district_phone = models.CharField(max_length=15, null=True, blank=True)
    department_name = models.CharField(max_length=250, null=True, blank=True)
    department_code = models.CharField(max_length=8, null=True, blank=True)
    department_phone = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    # def __str__(self):
    #     return f'{self.name_on_id} {self.national_id_number}'

