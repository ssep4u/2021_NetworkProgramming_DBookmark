from django.contrib import admin

from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('id', 'nickname', 'username')
    list_display_links = ('nickname', 'username')
    search_fields = ('nickname',)
