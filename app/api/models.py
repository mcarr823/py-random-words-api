from django.db import models

# Create your models here.

class Word(models.Model):
    text = models.CharField(max_length=30)
    length = models.IntegerField(default=0)

    def __str__(self):
        return self.text