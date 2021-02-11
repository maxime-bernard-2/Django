from django.contrib import admin

from app.models import Product, Tag, Image, Video, Like


class LikesInlineAdmin(admin.TabularInline):
    model = Product.like.through
    extra = 0


class TagsInlineAdmin(admin.TabularInline):
    model = Product.tags.through
    extra = 0


class ImageInlineAdmin(admin.TabularInline):
    model = Product.images.through
    extra = 0


class VideoInlineAdmin(admin.TabularInline):
    model = Product.videos.through
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = (TagsInlineAdmin, ImageInlineAdmin, VideoInlineAdmin, LikesInlineAdmin)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Image)
admin.site.register(Video)
