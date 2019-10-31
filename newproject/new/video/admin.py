from django.contrib import admin
from .models import Video

class videoAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Video ,videoAdmin)

