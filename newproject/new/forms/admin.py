from django.contrib import admin

from .models import Forms


#class FormAdmin(admin.ModelAdmin):
   # list_display = ('title',)

admin.site.register(Forms)


