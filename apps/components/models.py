from django.db import models

class ComponentFile(models.Model):
    
    FILE_TYPES = [
        ('.jsx', 'JavaScript XML'),
        ('.css', 'Cascading Style Sheets'),
    ]

    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    content = models.TextField(blank=True)

class Component(models.Model):
    name = models.CharField(max_length=255)
    files = models.ManyToManyField(ComponentFile)