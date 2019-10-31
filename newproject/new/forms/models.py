from django.db import models

class Forms(models.Model):
     title=models.CharField(max_length=100)
     description=models.TextField(blank=True, null=True, max_length=10000)
     price=models.DecimalField(decimal_places=2, max_digits= 10000)

     def __str__(self):
          return self.title
     class Meta:
        verbose_name_plural= "forms"


