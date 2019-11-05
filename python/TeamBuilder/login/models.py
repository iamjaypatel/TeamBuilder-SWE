from django.db import models


# Create your models here.
class Profile(models.Model):
    profile_username = models.CharField(
        max_length=60, primary_key=True, default='Username')
    profile_password = models.CharField(max_length=60, default='Password')
    profile_firstName = models.CharField(max_length=20, default='First Name')
    profile_lastName = models.CharField(max_length=20, default='Last Name')
    profile_Email = models.CharField(max_length=20, default='email@email.com')
    profile_PhoneNo = models.CharField(max_length=10, default='111-222-3333')


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_Admin = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_Name = models.CharField(max_length=60)
    project_Description = models.CharField(max_length=300)
    project_MaxCapacity = models.CharField(max_length=20)
    project_SpaceTaken = models.CharField(max_length=20)
    project_SpaceAvailable = models.CharField(max_length=10)


class Project_Involved(models.Model):
    profile_username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("profile_username", "project_id"),)
