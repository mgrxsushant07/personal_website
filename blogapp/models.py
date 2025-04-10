from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog_image = models.ImageField(upload_to='blog_images/', null=True, blank=True, default='default.jpg')

    def __str__(self):
        return self.title
    