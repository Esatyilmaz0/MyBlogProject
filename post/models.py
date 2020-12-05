from django.db import models
from core.sub_models.Category import Category
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

class Post(models.Model):
    author = models.ForeignKey('auth.user', related_name="posts", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)

    title = models.CharField(max_length=50, verbose_name="Title", unique=True, null=True, blank=False)
    content = RichTextField(verbose_name="Content", unique=True)
    description = models.TextField(verbose_name="Description", help_text="Meta Description Tag.", max_length=500,
                                   null=True, blank=True)

    image = models.ImageField(verbose_name="Image", null=True, blank=False)
    tags = models.CharField(max_length=999, verbose_name="Tags", null=False, blank=False,
                            help_text="Eg:django,django1,django2,...")

    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    slug = models.SlugField(editable=False)

    number_of_favourite = models.IntegerField(default=0)

    class Meta:
        ordering = ["created_date"]

    def tags_list(self):
        return self.tags.split(",")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Comment(models.Model):
    author = models.ForeignKey("auth.user", related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name="comments")

    content = models.TextField(verbose_name="Content")
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)

    def existing_comments(self):
        """
            Eğer Yeni Gelen Yorum Daha ÖNceden Var İse Onu Döndürür.
        :return: existing comment
        """
        return self.__class__.objects.filter(author=self.author, content=self.content, post=self.post)

    def save(self, *args, **kwargs):
        if len(self.existing_comments()) > 0:
            raise ValidationError("Your Comment already exists.")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.content

