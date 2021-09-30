from django.db import models
# Create your models here.


class register(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=8)

    class Meta:
        db_table = "register"

    def __str__(self):
        return self.name