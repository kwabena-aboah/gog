from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'is_active', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'national_id_number', 'digital_address',
            'mobile_number', 'region', 'district', 'district_code', 'district_phone',
            'department_name', 'department_code', 'department_phone')}
        ),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'national_id_number', 'digital_address',
            'mobile_number', 'region', 'district', 'district_code', 'district_phone',
            'department_name', 'department_code', 'department_phone'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



admin.site.register(User, UserAdmin)

