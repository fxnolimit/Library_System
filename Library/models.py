from django.db import models
import re

class BookManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data["title"]) <= 0:
            errors["title"] = "title name is required"
        if len(post_data["author"]) <= 0:
            errors["author"] = "author name is required"
        
        # email validation
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    year = models.DateField()
    pages = models.IntegerField()
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

    def __repr__(self):
        return f"{self.title} by {self.author}. Published in {self.year}"
