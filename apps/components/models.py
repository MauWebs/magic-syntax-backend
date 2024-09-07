from django.db import models
from core.constants.plans_constants import PLANS, FILE_TYPES, FOLDER_PATH


class Component(models.Model):
    name = models.CharField(max_length=255)
    plan = models.CharField(max_length=6, choices=PLANS)


class ComponentFile(models.Model):
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=255)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    plan = models.CharField(max_length=6, choices=PLANS, editable=False)
    file_type = models.CharField(max_length=4, choices=FILE_TYPES)
    folder_path = models.CharField(max_length=10, choices=FOLDER_PATH)

    def save(self, *args, **kwargs):
        if not self.plan:
            self.plan = self.component.plan
        super().save(*args, **kwargs)
