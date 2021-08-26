from django.db import models

# Create your models here.
class Project(models.Model):
  project = models.CharField(max_length=25)
  liveurl = models.CharField(max_length=50)
  giturl = models.CharField(max_length=50)
  image = models.CharField(max_length=100)
  description = models.CharField(max_length=75)

  def __str__(self):
        return self.name