from django.contrib import admin
from core.models import Profile

# Register your models here.


class MyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(Profile, MyAdmin)
