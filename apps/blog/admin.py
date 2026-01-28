# from django.contrib import admin
# from .models import BlogPost

# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'status', 'created_at')
#     list_filter = ('status', 'created_at')
#     search_fields = ('title', 'content', 'seo_title', 'seo_description')
#     prepopulated_fields = {'slug': ('title',)}
#     raw_id_fields = ('author',)
#     date_hierarchy = 'created_at'
#     ordering = ('status', 'created_at')

from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content', 'seo_title', 'seo_description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('author',)          # 🔐 make author read-only
    date_hierarchy = 'created_at'
    ordering = ('status', 'created_at')

    def save_model(self, request, obj, form, change):
        if not obj.pk:                      # only on CREATE
            obj.author = request.user       # auto-assign author
        super().save_model(request, obj, form, change)