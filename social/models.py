from django.db import models
from django.contrib.auth.models import User




class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    title = models.CharField(max_length=300)
    post_body = models.TextField()
    liked_count = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.title

