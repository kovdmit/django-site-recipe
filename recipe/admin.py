from django.contrib import admin
from .models import Recipe, Tag, Category, Quote


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'create_at', 'author', 'views', 'published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category')
    list_filter = ('category', )
    fields = ('title', 'slug', 'short_desc', 'proportions', 'content', 'photo', 'author', 'published', 'category', 'tags', 'create_at', 'views',)
    readonly_fields = ('create_at', 'views',)
    save_on_top = True
    save_as = True
    list_editable = ('published',)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Quote)

'''

©

'''