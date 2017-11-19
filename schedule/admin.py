from django.contrib import admin

# Register your models here.
from schedule.models import *


class ProfessorAdmin(admin.ModelAdmin):
    list_filter = ["position", "rank"]
    list_display = ["name", "position", "rank"]

class FacultyAdmin(admin.ModelAdmin):
    list_display = ["name", "key"]

class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ["name", "faculty"]
    list_filter = ["faculty"]

class StudySubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "type"]

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 3

class DaySchAdmin(admin.ModelAdmin):
    list_display = ["group", "day", "week"]
    list_filter = ["group", "day", "week"]
    inlines = (LessonInline,)

admin.site.register(Rank)
admin.site.register(Position)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(LectureRoom)
admin.site.register(StudyGroup, StudyGroupAdmin)
admin.site.register(StudySubject, StudySubjectAdmin)
admin.site.register(DaySchedule, DaySchAdmin)