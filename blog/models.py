from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, unique=True)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    image_banner = models.ImageField(upload_to='images/article/banner', blank=True, null=True)
    image_detail = models.ImageField(upload_to='images/article/detail', blank=True, null=True)
    active = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})


class Message(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} - {self.subject}'

