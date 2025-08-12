from django.contrib import admin
from .models import GPSLocation

@admin.register(GPSLocation)
class GPSLocationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the GPSLocation model.
    """
    list_display = ('user', 'latitude', 'longitude', 'altitude', 'accuracy', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'latitude', 'longitude')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
    readonly_fields = ('timestamp',)

    fieldsets = (
        (None, {
            'fields': ('user', 'latitude', 'longitude')
        }),
        ('Optional Fields', {
            'fields': ('altitude', 'accuracy')
        }),
        ('Metadata', {
            'fields': ('timestamp',)
        }),
    )

    def get_queryset(self, request):
        """
        Optimize queryset by selecting related user to avoid additional queries.
        """
        return super().get_queryset(request).select_related('user')