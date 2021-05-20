from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
from django.urls import reverse


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    img = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Card, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": self.slug})
