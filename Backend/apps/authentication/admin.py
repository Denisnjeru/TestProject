from django.contrib import admin
from .models import *
from django.contrib.auth.models import Permission
from django.template.loader import render_to_string
from django.contrib.auth.admin import UserAdmin


class  UsersAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'user_type')
    search_fields = ('username', 'email', 'user_type')

    fieldsets = (
        *UserAdmin.fieldsets,  
        ('Custom', {'fields': ('user_type',),},),
    )

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'render_picture','get_user_email','id_number')
    search_fields = ('user', 'get_user_email')

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = "User's email"

    def render_picture(self, obj):
        return render_to_string("widgets/picture.html", {"picture": obj.profile_pic})
    render_picture.short_description = "Profile Pic"

admin.site.register(Permission)
admin.site.register(Users, UsersAdmin)
admin.site.register(Profile, ProfileAdmin)