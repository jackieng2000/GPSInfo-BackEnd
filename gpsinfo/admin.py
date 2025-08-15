from django.contrib import admin
from .models import GPSLocation, GPSLatest

@admin.register(GPSLatest)
class GPSLatestAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude', 'timestamp', 'altitude', 'accuracy')
    list_filter = ('timestamp',)
    search_fields = ('user__username',)
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)

# Optionally, register GPSLocation if not already registered
@admin.register(GPSLocation)
class GPSLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude', 'timestamp', 'altitude', 'accuracy')
    list_filter = ('timestamp', 'user')
    search_fields = ('user__username',)
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)