from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from covidsaverr2app.models import covidappUser,Grad,Person,Restoran,appuser


class covidappUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(covidappUser, covidappUserAdmin)
admin.site.register(Grad)
admin.site.register(Restoran)
admin.site.register(Person)
admin.site.register(appuser)