from django.db import models
from datetime import datetime
# Create your models here.

STATUS = (
    (0, 'Draft'),
    (1, 'Published') 
)

class Poll(models.Model):
    title = models.CharField(max_length=200)
    question = models.CharField(max_length=200)
    active_until = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)
    def __str__(self):
        return self.title
    
class Option(models.Model):  
    title = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='Option', default=None)

    def __str__(self):
        return self.title

class Response(models.Model):
    name=models.CharField(max_length=200)
    response_time = models.DateTimeField(auto_now_add=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='Response', default=None)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='Response', default=None)
    def __str__(self):
        return self.name