from django.db import models


class UserProfile(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    hobbies = models.CharField(max_length=255)
    favorite_music = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    favorite_food = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname



