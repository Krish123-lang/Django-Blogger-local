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