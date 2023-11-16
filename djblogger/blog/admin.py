from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_at', 'status')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,PostAdmin)