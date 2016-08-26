from django.db import models
import uuid

class School(models.Model):
    """Schoool Model"""
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    # to String
    def __str__(self):
        return self.name.capitalize()

# Create your models here.
class Student(models.Model):
    """Student Model"""
    name = models.CharField(max_length=255, unique=True)
    marks = models.IntegerField()
    school = models.ForeignKey(School,null=True)
    uuid = models.CharField(max_length=255, null=True)

    # Override save
    def save(self, *args, **kwargs):
        self.uuid = uuid.uuid4()
        super().save(*args, **kwargs)
    # to String
    def __str__(self):
        return self.name.capitalize()
