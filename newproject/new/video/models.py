from django.db import models
from django.utils import timezone

class Video(models.Model):
 title=models.CharField(max_length=200)
 description=models.TextField(max_length=500)
 uploaddata=models.DateTimeField(default=timezone.now)
 video_id=models.CharField(max_length=50)
 tags=models.CharField(max_length=200)

 def __unicode__(self):
     return '/%s/' % self.title

 def get_absolute_url(self):
     return '/%s/' % self.title
