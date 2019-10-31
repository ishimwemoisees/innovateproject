from django.db import models

class home(models.Model):
 title=models.CharField(max_length=200)
 image=models.ImageField(upload_to="home")
 descrption=models.TextField(max_length=100)


