from django.db import models


class Hashtag(models.Model):
    hashtag = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)
    photo = models.ImageField(blank=True, null=True, upload_to="post_photo")
    hashtag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title

