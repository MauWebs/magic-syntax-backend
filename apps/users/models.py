from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from datetime import timedelta, datetime

from core.constants.plans_constants import PLANS, USERNAME_REGEX


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError(_("You must provide an email address"))
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")
        return self.create_user(email, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    user_name = models.CharField(max_length=150, validators=[USERNAME_REGEX])
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    plan = models.CharField(max_length=10, choices=PLANS, default="free")
    private_ip = models.CharField(max_length=45, blank=True, null=True)
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    arch = models.CharField(max_length=10, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    machine_id = models.CharField(max_length=255, blank=True, null=True)
    last_updated_device = models.DateTimeField(null=True, blank=True)
    updated_device_count = models.IntegerField(default=0)
    objects = CustomAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def can_update(self):
        now = datetime.now(timezone.utc)
        if self.last_updated_device is None:
            return True

        time_since_last_update = now - self.last_updated_device

        if time_since_last_update >= timedelta(seconds=5):
            self.updated_device_count = 0
            self.save()
            return True

        if self.updated_device_count < 2:
            return True

        return False