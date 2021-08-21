from django.contrib import admin
from .models import albumCategory,album,song,extendedUser
admin.site.register(albumCategory)
admin.site.register(album)
admin.site.register(song)
admin.site.register(extendedUser)