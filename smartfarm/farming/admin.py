from django.contrib import admin
from .models import Threat, CropTip, FarmerQuery


@admin.register(Threat)
class ThreatAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'severity', 'season']
    list_filter = ['category', 'severity']
    search_fields = ['name', 'description', 'affected_crops']


@admin.register(CropTip)
class CropTipAdmin(admin.ModelAdmin):
    list_display = ['title', 'crop_type', 'season', 'created_at']
    search_fields = ['title', 'content', 'crop_type']


@admin.register(FarmerQuery)
class FarmerQueryAdmin(admin.ModelAdmin):
    list_display = ['name', 'crop', 'category', 'answered', 'created_at']
    list_filter = ['category', 'answered']
    search_fields = ['name', 'crop', 'problem']

from .models import CommunityPost

@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'crop', 'category', 'likes', 'is_approved', 'created_at']
    list_filter = ['category', 'is_approved', 'state']
    search_fields = ['name', 'content', 'crop']
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(is_approved=True)
    approve_posts.short_description = "Approve selected posts"
