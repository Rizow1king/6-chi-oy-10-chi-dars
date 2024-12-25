from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'views', "created_at")
    list_display_links = ("id", "name")
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ('name',)
    search_fields = ('name',)
    readonly_fields = ("views",)


class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "teacher", "theme", "published", "course")
    list_display_links = ("id", "name", "teacher")
    list_per_page = 5
    list_editable = ("theme",)
    list_filter = ("course", "published", "teacher")
    actions_on_top = False
    actions_on_bottom = True
    search_fields = ("description", "name", "teacher")


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
