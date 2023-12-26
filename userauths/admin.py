from django.contrib import admin
from userauths.models import User, Profile, ContactUs
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'message']


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(ContactUs, ContactUsAdmin)

