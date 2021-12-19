from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('title_detail', kwargs={'pk': self.pk})