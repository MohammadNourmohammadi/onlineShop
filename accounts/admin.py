from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAddress, MyUser
from .forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):
    # add_form = UserCreationForm
    # form = UserChangeForm
    model = MyUser
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'is_staff', 'is_active', 'is_delivery_man')
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_delivery_man')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(UserAddress)
