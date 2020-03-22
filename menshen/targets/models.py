from django.db import models
from django.urls import reverse

class Target(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('target_view', args=[str(self.id)])
    def get_edit_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('target_edit', args=[str(self.id)])
    def __str__(self):
        return self.name

