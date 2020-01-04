from django.contrib import admin

from .models import SocialNetwork, SocialNetworkLink


class SocialNetworkLinkInline(admin.TabularInline):
    model = SocialNetworkLink
    extra = 1


admin.site.register(SocialNetwork)
