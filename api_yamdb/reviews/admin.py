from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from reviews.models import Category, Comment, Genre, Review, Title

User = get_user_model()

admin.site.register(User, UserAdmin)
admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Genre, admin.ModelAdmin)
admin.site.register(Title, admin.ModelAdmin)
admin.site.register(Review, admin.ModelAdmin)
admin.site.register(Comment, admin.ModelAdmin)
