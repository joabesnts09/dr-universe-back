from django.db import models
import uuid


class Events(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField()
    imgUrl = models.URLField(max_length=200)
    dateEvent = models.CharField(max_length=10)
    timeEvent = models.CharField(max_length=10)