from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserCustom

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserCustom
    list_display = ('username', 'email', 'is_superuser', 'is_staff', 'rol')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rol',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('rol',)}),
    )

admin.site.register(UserCustom, CustomUserAdmin)




