from django.db import models
import secrets
from apps.users.models import User


class ApiKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    key = models.CharField(max_length=40, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_urlsafe(32)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.key
