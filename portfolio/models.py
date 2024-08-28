from django.db import models

# Create your models here.
class Settings(models.Model):
    site_title = models.CharField(max_length=255)
    site_logo = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    cover_title = models.CharField(max_length=255)
    cover_desc = models.TextField()
    about_title = models.CharField(max_length=255)
    about_desc = models.TextField()
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    github = models.CharField(max_length=255)

class Services(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    color = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)