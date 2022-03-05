from django.contrib import admin
from .models import CustomUser
#  import standard user model
from django.contrib.auth.models import User

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'role')
    search_fields = ('phone', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)
# admin.site.register(CustomUser, UserAdmin)