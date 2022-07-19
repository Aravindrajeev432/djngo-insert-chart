from django.db import models

# Create your models here.
class Colors(models.Model):
    color_red = models.IntegerField()
    color_blue = models.IntegerField()
    color_yellow = models.IntegerField()
    color_green = models.IntegerField()
    color_purple = models.IntegerField()
    color_orange = models.IntegerField()
