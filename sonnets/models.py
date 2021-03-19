from django.db import models


class Sonnet(models.Model):
    number = models.CharField(max_length=4)
    text = models.TextField()
