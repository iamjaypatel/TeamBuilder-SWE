from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Profile(models.Model):
    username_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]$', message="1. Cannot start or have  '_' or '.' together, only be used once \n 2. Length must be between 8 to 20 characters. \n 3. Only contains alphanumeric characters, '.' and '_' ")
    profile_username = models.CharField(
        'Username', validators=[username_regex], max_length=20, primary_key=True)
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
    project_Description = models.TextField('Description', max_length=300)
    project_MaxCapacity = models.PositiveIntegerField(
        'Maximum Capacity', default=10)
    project_SpaceTaken = models.PositiveIntegerField(
        'Space Taken', default=1)
    project_SpaceAvailable = models.PositiveIntegerField(
        blank=True, editable=True)
    # Space 1: Admin
    # Space 2-9, Profile.


class Project_Involved(models.Model):
    profile_username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_accepted = models.BooleanField(default=False)
    class Meta:
        unique_together = (("profile_username", "project_id"),)
