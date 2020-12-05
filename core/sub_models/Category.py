from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(editable=False)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)