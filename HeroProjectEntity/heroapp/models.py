from django.db import models

# Create your models here.
class Hero(models.Model):
    hero_name = models.CharField(max_length=69)
    role = models.CharField(max_length=12)

    def __str__(self):
        return self.hero_name