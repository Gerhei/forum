from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from src.users.models import User, Account

admin.site.register(User, UserAdmin)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'reputation')
    fields = ('user', 'slug', 'reputation', 'description')
    readonly_fields = ('slug',)
    search_fields = ('user__username',)
