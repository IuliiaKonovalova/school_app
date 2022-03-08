from django.contrib import admin
from .models import CustomUser, Teacher, Receptionist, SalesManager, Parent
#  import standard user model
from django.contrib.auth.models import User

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'role')
    search_fields = ('phone', 'first_name', 'last_name')


@admin.register(Parent)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'relation', 'address')
    search_fields = ('user', 'relation', 'address')


admin.site.register(User, UserAdmin)
admin.site.register(User, Parent)
# admin.site.register(CustomUser, UserAdmin)