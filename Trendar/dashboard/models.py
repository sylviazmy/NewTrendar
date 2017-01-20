from django.db import models

# Create your models here.

class in_extract_tags(models.Model):
    name = models.CharField(max_length=10)
    rank = models.FloatField(default=0)

class in_textrank(models.Model):
    name = models.CharField(max_length=10)
    rank = models.FloatField(default=0)

class latest(models.Model):
    summary = models.CharField(max_length=150)
    date = models.DateTimeField()


class sentiment(models.Model):
    number = models.IntegerField(default=0)

class neg_total(models.Model):
    typeof = models.CharField(max_length=10)
    number = models.IntegerField(default=0)

class negative(models.Model):
    typeof = models.CharField(max_length=10)
    score = models.FloatField(default=0)
    content = models.CharField(max_length=100)
    def __str__(self):
    # 在Python3中使用 def __str__(self)
        return self.typeof