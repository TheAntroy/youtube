import uuid
from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.DateField()
    GENRE_CHOICES = [
        ("fantasy", "Fantasy"),
        ("fiction", "Fiction"),
        ("classic", "Classic"),
        ("romance", "Romance"),
        ("mystery", "Mystery"),
        ("technology", "Technology"),
    ]
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES)
    contact = models.EmailField(max_length=255)
    images = models.URLField(
        default="https://preline.co/docs/assets/img/500x300/img1.jpg"
    )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )

    def __str__(self):
        return self.title
