from django.db import models

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    year = models.DateField()
    pages = models.IntegerField()
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.title} by {self.author}. Published in {self.year}"
