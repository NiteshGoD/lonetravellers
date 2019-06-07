from django.contrib import admin
from .models import Project, Comment
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)
