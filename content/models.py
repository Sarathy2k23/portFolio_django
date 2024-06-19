from django.db import models



class content(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/')

