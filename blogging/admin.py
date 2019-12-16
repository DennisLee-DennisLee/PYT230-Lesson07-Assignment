from django.contrib import admin

from blogging.models import Post, Category , PostAdmin , CategoryAdmin , CategoryInline


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
