from django.db import models

# Create your models here.


class Counter(models.Model):
    count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}"
