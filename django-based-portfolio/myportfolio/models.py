from django.db import models

# Create your models here.
class Skills(models.Model):
    language = models.CharField(max_length=50, blank=True)
    libraries = models.CharField(max_length=100, blank=True)
    database = models.CharField(max_length=100, blank=True)
    ml = models.CharField(max_length=100, blank=True)

    def __str__(self): 
        return "Skill Added!"
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self): 
        return self.title
    