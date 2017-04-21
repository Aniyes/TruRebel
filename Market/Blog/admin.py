from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):

    blog_display = ['__str__','title','blog_post']
    blog_editable = ['title']

    class Meta:

        model = Blog

admin.site.register(Blog, BlogAdmin),
