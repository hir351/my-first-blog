# pylint: disable=C0103

from django.contrib import admin
from .models import Post

admin.site.register(Post)
