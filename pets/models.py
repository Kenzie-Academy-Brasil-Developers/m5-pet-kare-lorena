from django.db import models

# Create your models here.
class PetSex(models.TextChoices):
    MALE = 'Male'
    FEMALE = 'Female'
    NOT_INFORMED = 'Not Informed'

class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20,
        choices=PetSex.choices,
        default=PetSex.NOT_INFORMED
    )