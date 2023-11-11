# Create app inside djblogger
- create `blog` folder inside `djblogger(project)`
`python3 manage.py startapp blog ./djblogger/blog`

- update `base.py`
```
INSTALLED_APPS = [
    "djblogger.blog",
    ...
]
```
- update `blog/app.py`
```
class BlogConfig(AppConfig):
    ...
    name = "djblogger.blog"
```
1. `blog/models.py`
```
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")

    class Meta:
        ordering = ("-updated_at", )

    def __str__(self):
        return self.title
```
2. `blog/admin.py`
```
from django.contrib import admin
from .models import Post
admin.site.register(Post)
```