from django.contrib import admin

from .models import TrainingDay, TrainingDayRoute


class TrainingDayRouteInline(admin.TabularInline):
    model = TrainingDayRoute
    extra = 1


@admin.register(TrainingDay)
class TrainingDayAdmin(admin.ModelAdmin):
    inlines = (TrainingDayRouteInline,)
