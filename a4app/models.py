from django.db import models

# Create your models here.


class User(models.Model):
    login_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.IntegerField()
    vege_type = models.CharField(max_length=30)
    alle_type = models.CharField(max_length=50)
    metabolism = models.IntegerField()

    def __str__(self) -> str:
        return self.login_id
