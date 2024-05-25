from django.contrib import admin
from .models import NewsModel, CategoryModel, ContactModel

#admin.site.register(NewsModel)
admin.site.register(ContactModel)
admin.site.register(CategoryModel)

@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'slug',  'published_time', 'status']
    list_filter = ['status', 'created_time', 'published_time', 'category']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'published_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'published_time']

