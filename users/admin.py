from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    # admin/users/user field value
    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("gender", "language", "currency", "superhost")
