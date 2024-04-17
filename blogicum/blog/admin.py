from django.contrib import admin
from .models import Category, Location, Post


admin.site.empty_value_display = '---'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'text',
        'category',
        'location',
        'created_at',
        'is_published',
        'pub_date'
    )
    list_editable = (
        'is_published',
        'category'
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'category',
    )
    list_display_links = (
        'title',
    )


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
    )


admin.site.register(Location)
