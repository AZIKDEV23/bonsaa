from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.FileField("media/image/")

    def __str__(self):
        return self.title
    