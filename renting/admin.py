from django.contrib import admin
from .models import (
    TrekkingGear,
    Camera,
    RidingGear,
    ActionCamera,
    GamingConsole,
    WinterWear,
    AudioVisualEquipment,
    CampingGear,
    CreatorGear
)

@admin.register(TrekkingGear)
class TrekkingGearAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('availability',)
    ordering = ('name',)
    list_per_page = 20

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('name', 'camera_type', 'description', 'price', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('camera_type', 'availability')
    ordering = ('name',)
    list_per_page = 20

@admin.register(RidingGear)
class RidingGearAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('availability',)
    ordering = ('name',)
    list_per_page = 20

@admin.register(ActionCamera)
class ActionCameraAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'description', 'price', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('brand', 'availability')
    ordering = ('name',)
    list_per_page = 20

@admin.register(GamingConsole)
class GamingConsoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('name', 'availability')
    ordering = ('name',)
    list_per_page = 20

@admin.register(WinterWear)
class WinterWearAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('availability',)
    ordering = ('name',)
    list_per_page = 20

@admin.register(AudioVisualEquipment)
class AudioVisualEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'equipment_type', 'description', 'price', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('equipment_type', 'availability')
    ordering = ('name',)
    list_per_page = 20

@admin.register(CampingGear)
class CampingGearAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('availability',)
    ordering = ('name',)
    list_per_page = 20

@admin.register(CreatorGear)
class CreatorGearAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('availability',)
    ordering = ('name',)
    list_per_page = 20
