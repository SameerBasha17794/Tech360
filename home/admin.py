from django.contrib import admin
from .models import MainBanner,Course,SubCourse,CourseContent,Blog


admin.site.register(MainBanner)
admin.site.register(Course)
admin.site.register(SubCourse)
admin.site.register(CourseContent)
admin.site.register(Blog)