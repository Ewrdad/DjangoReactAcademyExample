from django.db import models

# Create your models here.
class blogPost(models.Model):
    postID = models.AutoField(primary_key=True)
    postTitle = models.CharField(max_length=200)
    postBulk = models.CharField(max_length=500)
    postPic = models.CharField(max_length=200)