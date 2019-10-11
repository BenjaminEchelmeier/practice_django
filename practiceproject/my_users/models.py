from django.db import models

# Create your models here.


class Users(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return f"{str(self.first)} {str(self.last)}"
