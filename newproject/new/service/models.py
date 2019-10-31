from django.db import models
from django.utils import timezone


class Service(models.Model):
 title=models.CharField(max_length=100)
 image=models.ImageField(upload_to='Service')
 descrption=models.CharField(max_length=500)
 uploaddata=models.DateTimeField(default=timezone.now)

 def __str__(self):
     return self.title
 class Meta:
     verbose_name_plural= "services"


