from django.contrib import admin
from .models import Climbingwall, ClimbingwallPhoto
from contacts.admin import EmailInline, PhoneNumberInline
from social_networks.admin import SocialNetworkLinkInline
from timetable.admin import TimetableInline


class ClimbingwallPhotoInline(admin.TabularInline):
    model = ClimbingwallPhoto
    extra = 3


@admin.register(Climbingwall)
class ClimbingwallAdmin(admin.ModelAdmin):
    inlines = (
        EmailInline,
        PhoneNumberInline,
        SocialNetworkLinkInline,
        ClimbingwallPhotoInline,
        TimetableInline
    )
