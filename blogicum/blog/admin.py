from django.contrib import admin
from .models import Category, Location, Post


admin.site.empty_value_display = '---'


# насчет коммента про регистрацию моделей через декораторы
# @admin.register(site=admin.site)
# так не выходит, ссылка на стак не особо помогла
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


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Location)
