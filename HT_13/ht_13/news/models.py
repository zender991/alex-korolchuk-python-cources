from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.category_name



class Story(models.Model):
    author = models.CharField(max_length=100, default='')
    descendants = models.CharField(max_length=100, default='')
    story_id = models.CharField(max_length=100, default='')
    kids = models.TextField(default='')
    score = models.IntegerField(default=0)
    text = models.TextField(default='')
    time = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100, default='')
    url = models.URLField()
    category_id = models.ForeignKey(Category, on_delete=models
                                    .CASCADE)

    def __str__(self):
        return self.title
