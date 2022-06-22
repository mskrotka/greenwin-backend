from django.contrib import admin

from .models import Lead
# Register your models here.
@admin.register(Lead)
class UserExtraDataAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone",
        "info",
    ]