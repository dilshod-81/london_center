from django.db import models
from django.urls import reverse
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=NewsModel.Status.Published)
class CategoryModel(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class NewsModel(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='media/news_image/images')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft)
    published = PublishedManager()
    class Meta:
        ordering = ['-published_time']
    def get_absulute_url(self):
        return reverse('news_detail', args=[self.slug])
    def __str__(self):
        return self.title

class ContactModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email


