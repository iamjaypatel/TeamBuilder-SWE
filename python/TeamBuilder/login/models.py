from django.db import models

# Create your models here.
class Profile(models.Model):
#    profileID = models.CharField( primary_key=True)
   userName = models.CharField(max_length = 20)
   userPassword = models.CharField(max_length = 60)
# class Projects(models.Model):
#    pass
# class Project_Involved(models.Model):
#    pass