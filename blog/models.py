from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("제목", max_length=50)
    content = models.TextField("내용")
    thumbnail = models.ImageField("썸네일", upload_to="post", blank="True")
    
    def __str__(self):
        return f"{self.title}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField("댓글")
    
    def __str__(self):
        return f"post: {self.post}, comment: {self.comment}"