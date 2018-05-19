from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, blank=True, null=True)
    summary = models.TextField(null=True)
    url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.title
