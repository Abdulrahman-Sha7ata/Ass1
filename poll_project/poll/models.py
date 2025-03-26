from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

STATUS = (
    (0, 'Draft'),
    (1, 'Published') 
)

class Poll(models.Model):
    title = models.CharField(max_length=200)
    question = models.CharField(max_length=200)
    active_until = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    def __str__(self):
        return f"{self.title} - {self.question} (Active until: {self.active_until}, Status: {self.status})"
    

class Option(models.Model):  
    title = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options', default=None)

    def __str__(self):
        return self.title

class Response(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='responses', default=None)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='responses', default=None)
    name=models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now, editable=True)
    
    def __str__(self):
        return f"Response  {self.name}  Option {self.option.title} at {self.created_at}"