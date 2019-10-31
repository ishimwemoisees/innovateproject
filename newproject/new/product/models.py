from django.db import models

from django.utils import timezone
class Product(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField(max_length=10000)
    price=models.DecimalField(decimal_places=3, max_digits=1000)
    timecreated=models.DateTimeField(default=timezone.now)
    featured=models.BooleanField()
    def __str__(self):
      return self.title

