from django.contrib import admin
from .models import Route, RoutePhoto


class RoutePhotoInline(admin.TabularInline):
    model = RoutePhoto
    extra = 3


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    inlines = (
        RoutePhotoInline,
    )
