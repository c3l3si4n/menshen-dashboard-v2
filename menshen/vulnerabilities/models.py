from django.db import models

# Create your models here.


class Vulnerability(models.Model):
    target = models.ForeignKey('targets.Target', on_delete=models.CASCADE)
    cve = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255)
    date_found = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_name

