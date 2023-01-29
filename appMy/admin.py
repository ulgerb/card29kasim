from django.contrib import admin
from .models import *

# Register your models here.


class CommentAdmin(admin.ModelAdmin):

    list_display = ('card','name','title','date_now')
    list_filter = ('date_now',)
    search_fields = ('title', 'name', 'card__title')


admin.site.register(Card)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
