from django.db import models
from django.conf import settings

LANGUAGE_CHOICES = (
    (1, "KOR"),
    (2, "ENG"),
    (3, "JAN"),
    (4, "CHN"),
)


class Tag(models.Model):
    name = models.CharField(max_length=50)
        
    def __str__(self):
        return self.name
   

class Post(models.Model):
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='posts'
)
    
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    language = models.IntegerField(choices=LANGUAGE_CHOICES)

    photo = models.ImageField(
        upload_to='post_photo/',
        blank=True,
        null=True
    )
    
    tags = models.ManyToManyField(
        Tag,
        related_name='posts'
    )

    def __str__(self):
        return self.title
    

