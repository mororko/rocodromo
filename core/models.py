from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=120)
    body = models.CharField(max_length=240, blank=True)
    is_active = models.BooleanField(default=True)

    start_at = models.DateTimeField()
    end_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-start_at"]

    def __str__(self):
        return self.title
