# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post

# Register your models here.
class PostDB(admin.ModelAdmin):
    list_display = [
       "Title","Text","Author","Created_date","Published_date" 
    ]
    admin.site.register(Post)