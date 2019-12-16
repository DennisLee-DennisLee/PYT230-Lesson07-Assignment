from django.contrib import admin

from blogging.models import Post, Category , PostAdmin , CategoryAdmin , CategoryInline


# admin.site.register(Post)
# admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(PostAdmin)
# admin.site.register(CategoryAdmin)
# admin.site.register(CategoryInline)
