from django.contrib import admin

# Register your models here.
from .models import astro, blogPost

admin.site.register(blogPost)
admin.site.register(astro)