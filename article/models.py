from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    CHOICES = ((None, 'Select a category'), ('Food', 'Food'), ('Economy', 'Economy'),
               ('International', 'International'),
               ('News', 'News'), ('Music', 'Music'),
               ('Sport', 'Sport'), ('Technology', 'Technology'), ('Health', 'Health'))
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CHOICES, default=None, blank=False, null=False)
    content = models.TextField()
    image = models.FileField(upload_to='article/image/')
    date_created = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
