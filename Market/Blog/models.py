from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=400)
    blog_post = models.TextField()

    def __str__(self):
        return self.title