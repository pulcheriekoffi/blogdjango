from django.contrib import admin

# Register your models here.
from .models import Post
#import les fonctions
#enregistre 
admin.site.register(Post)
