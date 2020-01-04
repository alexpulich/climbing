from django.contrib import admin
from .models import Email, PhoneNumber


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1
