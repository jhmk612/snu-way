from django.contrib import admin

from .models import Post, Vehicle, Location, Rating

from .forms import PostForm

class PostAdmin(admin.ModelAdmin):
    form=PostForm

admin.site.register(Post, PostAdmin)

admin.site.register(Vehicle)

admin.site.register(Location)

admin.site.register(Rating)
