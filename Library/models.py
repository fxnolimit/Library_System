from django.db import models

class Books(models.Model):
    title = models.TextField()
    author = models.TextField()
    year = models.DateTimeField()
    pages = models.IntegerField()
    description = models.CharField(300)

    def __repr__(self):
        return f"{self.title} by {self.author}. Published in {self.year}"
