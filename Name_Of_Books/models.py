from django.db import models


class Novels(models.Model):
    name = models.CharField(max_length=200)