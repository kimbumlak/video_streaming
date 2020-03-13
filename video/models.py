from django.db import models
from django.contrib.auth.models import User
import string, random

# Create your models here.

def user_directory_path(instance, filename):
    random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return '{0}{1}'.format(random_char, filename)

class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    #path = models.CharField(max_length=60)
    #file = models.FileField(default="")
    file = models.FileField(upload_to=user_directory_path)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False) #todo: auto_now=True
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True,blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

