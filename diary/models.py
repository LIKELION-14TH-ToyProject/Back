from django.db import models

LANGUAGE_CHOICES = (
    (1, "KOR"),
    (2, "ENG"),
    (3, "JAN"),
    (4, "CHN"),
)



class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    language = models.IntegerField(choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text[:20]
    
