from django.db import models

# Create your models here.
class blogPost(models.Model):
    postID = models.AutoField(primary_key=True)
    postTitle = models.CharField(max_length=200)
    postBulk = models.CharField(max_length=500)
    postPic = models.CharField(max_length=200)


class astro(models.Model):
    astroID = models.AutoField(primary_key=True)
    astroName = models.CharField(max_length=200)
    astroCraft = models.CharField(max_length=400)
    astroDay = models.IntegerField(default=50)
    astroMonth = models.IntegerField(default=50)
    astroYear = models.IntegerField(default=50)