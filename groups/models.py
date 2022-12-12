from django.db import models

# Create your models here.
class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    pet = models.ForeignKey(
        'pets.Pet', on_delete=models.CASCADE, related_name='group'
    )