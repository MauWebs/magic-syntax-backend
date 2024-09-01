from django.db import models

FILE_TYPES = [
    ('.jsx', 'JavaScript XML'),
    ('.css', 'Cascading Style Sheets'),
]

PLAN_TYPES = [
    ('free', 'Free'),
    ('basic', 'Basic'),
    ('expert', 'Expert'),
]


class ComponentFile(models.Model):
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    content = models.TextField(blank=True)
    plan = models.CharField(max_length=10, choices=PLAN_TYPES)


class Component(models.Model):
    name = models.CharField(max_length=255)
    files = models.ManyToManyField(ComponentFile)
    plan = models.CharField(max_length=10, choices=PLAN_TYPES)
