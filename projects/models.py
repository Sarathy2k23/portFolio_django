from django.db import models


class projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects_images/')


# Create your models here.
