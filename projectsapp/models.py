from django.db import models

# Create your models here.
class Project(models.Model):
  project = models.CharField(max_length=50)
  liveurl = models.CharField(max_length=75)
  giturl = models.CharField(max_length=75)
  image = models.CharField(max_length=150)
  description = models.CharField(max_length=100)

  def __str__(self):
        return self.project