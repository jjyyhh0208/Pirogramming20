from django.db import models

# Create your models here.
class DevTool (models.Model):
    name = models.CharField(max_length=24)
    kind = models.CharField(max_length=24)
    content = models.TextField(max_length=200)

    def __str__ (self):
        return self.name