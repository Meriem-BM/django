from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

FIELD = (
    (0,"Frontend Design"),
    (1,"Python Programmes"),
    (2, "Django Development"),
    (3, "Article")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    tags = models.TextField()
    location = models.TextField()
    field = models.IntegerField(choices=FIELD, default=0)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.FileField(upload_to='templates/blogs/', validators=[FileExtensionValidator( ['html'] ) ])
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='media/uploads/images/')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title