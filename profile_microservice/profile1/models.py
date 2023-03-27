from django.db import models

class UserProfile(models.Model):
    user_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    