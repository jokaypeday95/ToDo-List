from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.TextField(max_length=300)
    status = models.BooleanField(default=False)

    def __str__(self):
        return '%s: %s' % (self.id, self.title)