from django.db import models

# Create your models here.
# class Album(models.Model):
#       name = models.CharField(max_length=100)
#       # artist = models.ForeignKey(Artists) 
#       release_date = models.DateField()

class User_Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    def __str__(self):
        return self.subject