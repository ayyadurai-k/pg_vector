from django.db import models
from pgvector.django import VectorField

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    embedding = VectorField(dimensions=384,null=True, blank=True)  # set dimension size according to your vector model