from django.db import models
from django.conf import settings

class Hashtag(models.Model):
    hashtag = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag
    
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=500)
    photo = models.ImageField(blank=True, null=True, upload_to="post_photo")
    hashtag = models.ManyToManyField(Hashtag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

