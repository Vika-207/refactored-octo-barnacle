from django.contrib import admin

# Register your models here.
rom django.contrib import admin
from blogs.models import Post, Commit

Register your models here.
#admin.site.register(Post)
#admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(admin. ModelAdmin):
list_display = ('name', 'email', 'post', 'created', 'active')
list_filter = ('active', 'created', 'updated')
search_fields = ('name', 'email', 'body')

@admin.register(Post)
class PostAdmin(admin ModelAdmin):
list_display = ('title', 'slug', 'author', 'date_posted', 'status')
list_filter = ('status', 'created', 'date_posted', 'author')
search_fields = ('title', 'content')
prepopulated_fields = {'slug': 'title',)}
raw_id_fields = ('author',)
data_hierarchy = 'date_posted'
ordering = ('status', 'date_posted').
