from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed']


# Create your models here.
