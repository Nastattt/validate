from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    photo = models.FileField()


    def __str__(self):
        return self.name
class Posts(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=30)