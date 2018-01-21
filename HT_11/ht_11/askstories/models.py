from django.db import models

class Askstories(models.Model):
    author = models.CharField(max_length=200)
    descendants = models.CharField(max_length=200)
    story_id = models.CharField(max_length=200)
    kids = models.CharField(max_length=500)
    score = models.IntegerField(default=0)
    text = models.TextField(default='default')
    time = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

