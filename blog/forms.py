from django.db.models import fields
from django.forms import ModelForm 
from blog.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'description', 'location', 'author', 'field', 'content', 'tags', 'status', 'image']
