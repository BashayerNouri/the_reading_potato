from django.contrib import admin
from .models import Article, Contribution, Change

# Register your models here.
admin.site.register(Article)
admin.site.register(Contribution)
admin.site.register(Change)

