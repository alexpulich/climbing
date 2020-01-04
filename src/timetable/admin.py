from django.contrib import admin

from .models import Timetable


class TimetableInline(admin.TabularInline):
    model = Timetable
    extra = 7
    max_num = 7
