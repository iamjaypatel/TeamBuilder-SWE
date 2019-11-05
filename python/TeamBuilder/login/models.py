from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Profile(models.Model):
    profile_username = models.CharField('Username',
                                        max_length=60, primary_key=True)
    profile_password = models.CharField(
        'Password', max_length=60)
    profile_firstName = models.CharField(
        'First Name', max_length=20)
    profile_lastName = models.CharField(
        'Last Name', max_length=20)
    profile_Email = models.EmailField(
        'E-mail Address', max_length=20)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    profile_PhoneNo = models.CharField('Phone Number',
                                       validators=[phone_regex], max_length=17, blank=True)


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_Admin = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_Name = models.CharField('Name', max_length=60)
    project_Description = models.CharField('Description', max_length=300)
    project_MaxCapacity = models.IntegerField(
        'Maximum Capacity', default=10, editable=False)
    project_SpaceTaken = models.IntegerField(
        'Space Taken', default=1, editable=False)
    project_SpaceAvailable = models.IntegerField(blank=True, editable=False)


class Project_Involved(models.Model):
    profile_username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("profile_username", "project_id"),)
