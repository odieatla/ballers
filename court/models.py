from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    birthdate = models.DateField(blank=True, null=True)

    def __unicide__(self):
        return self.user.username
