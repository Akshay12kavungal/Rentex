from django.urls import path
from .views import (
    TrekkingGearListView, TrekkingGearDetailView, TrekkingGearCreateView, TrekkingGearUpdateView, TrekkingGearDeleteView,
    CameraListView, CameraDetailView, CameraCreateView, CameraUpdateView, CameraDeleteView,
    RidingGearListView, RidingGearDetailView, RidingGearCreateView, RidingGearUpdateView, RidingGearDeleteView,
    ActionCameraListView, ActionCameraDetailView, ActionCameraCreateView, ActionCameraUpdateView, ActionCameraDeleteView,
    GamingConsoleListView, GamingConsoleDetailView, GamingConsoleCreateView, GamingConsoleUpdateView, GamingConsoleDeleteView,
    WinterWearListView, WinterWearDetailView, WinterWearCreateView, WinterWearUpdateView, WinterWearDeleteView,
    AudioVisualEquipmentListView, AudioVisualEquipmentDetailView, AudioVisualEquipmentCreateView, AudioVisualEquipmentUpdateView, AudioVisualEquipmentDeleteView,
    CampingGearListView, CampingGearDetailView, CampingGearCreateView, CampingGearUpdateView, CampingGearDeleteView,
    CreatorGearListView, CreatorGearDetailView, CreatorGearCreateView, CreatorGearUpdateView, CreatorGearDeleteView,
    home
)

urlpatterns = [
    # Home
    path('home', home, name='home'),

    # Trekking Gear
    path('trekkinggear/', TrekkingGearListView.as_view(), name='trekkinggear_list'),
    path('trekkinggear/<int:pk>/', TrekkingGearDetailView.as_view(), name='trekkinggear_detail'),
    path('trekkinggear/add/', TrekkingGearCreateView.as_view(), name='trekkinggear_add'),
    path('trekkinggear/<int:pk>/edit/', TrekkingGearUpdateView.as_view(), name='trekkinggear_update'),
    path('trekkinggear/<int:pk>/delete/', TrekkingGearDeleteView.as_view(), name='trekkinggear_delete'),

    # Camera
    path('camera/', CameraListView.as_view(), name='camera_list'),
    path('camera/<int:pk>/', CameraDetailView.as_view(), name='camera_detail'),
    path('camera/add/', CameraCreateView.as_view(), name='camera_add'),
    path('camera/<int:pk>/edit/', CameraUpdateView.as_view(), name='camera_update'),
    path('camera/<int:pk>/delete/', CameraDeleteView.as_view(), name='camera_delete'),

    # Riding Gear
    path('ridinggear/', RidingGearListView.as_view(), name='ridinggear_list'),
    path('ridinggear/<int:pk>/', RidingGearDetailView.as_view(), name='ridinggear_detail'),
    path('ridinggear/add/', RidingGearCreateView.as_view(), name='ridinggear_add'),
    path('ridinggear/<int:pk>/edit/', RidingGearUpdateView.as_view(), name='ridinggear_update'),
    path('ridinggear/<int:pk>/delete/', RidingGearDeleteView.as_view(), name='ridinggear_delete'),

    # Action Camera
    path('actioncamera/', ActionCameraListView.as_view(), name='actioncamera_list'),
    path('actioncamera/<int:pk>/', ActionCameraDetailView.as_view(), name='actioncamera_detail'),
    path('actioncamera/add/', ActionCameraCreateView.as_view(), name='actioncamera_add'),
    path('actioncamera/<int:pk>/edit/', ActionCameraUpdateView.as_view(), name='actioncamera_update'),
    path('actioncamera/<int:pk>/delete/', ActionCameraDeleteView.as_view(), name='actioncamera_delete'),

    # Gaming Console
    path('gamingconsole/', GamingConsoleListView.as_view(), name='gamingconsole_list'),
    path('gamingconsole/<int:pk>/', GamingConsoleDetailView.as_view(), name='gamingconsole_detail'),
    path('gamingconsole/add/', GamingConsoleCreateView.as_view(), name='gamingconsole_add'),
    path('gamingconsole/<int:pk>/edit/', GamingConsoleUpdateView.as_view(), name='gamingconsole_update'),
    path('gamingconsole/<int:pk>/delete/', GamingConsoleDeleteView.as_view(), name='gamingconsole_delete'),

    # Winter Wear
    path('winterwear/', WinterWearListView.as_view(), name='winterwear_list'),
    path('winterwear/<int:pk>/', WinterWearDetailView.as_view(), name='winterwear_detail'),
    path('winterwear/add/', WinterWearCreateView.as_view(), name='winterwear_add'),
    path('winterwear/<int:pk>/edit/', WinterWearUpdateView.as_view(), name='winterwear_update'),
    path('winterwear/<int:pk>/delete/', WinterWearDeleteView.as_view(), name='winterwear_delete'),

    # Audio-Visual Equipment
    path('audiovisual/', AudioVisualEquipmentListView.as_view(), name='audiovisual_list'),
    path('audiovisual/<int:pk>/', AudioVisualEquipmentDetailView.as_view(), name='audiovisual_detail'),
    path('audiovisual/add/', AudioVisualEquipmentCreateView.as_view(), name='audiovisual_add'),
    path('audiovisual/<int:pk>/edit/', AudioVisualEquipmentUpdateView.as_view(), name='audiovisual_update'),
    path('audiovisual/<int:pk>/delete/', AudioVisualEquipmentDeleteView.as_view(), name='audiovisual_delete'),

    # Camping Gear
    path('campinggear/', CampingGearListView.as_view(), name='campinggear_list'),
    path('campinggear/<int:pk>/', CampingGearDetailView.as_view(), name='campinggear_detail'),
    path('campinggear/add/', CampingGearCreateView.as_view(), name='campinggear_add'),
    path('campinggear/<int:pk>/edit/', CampingGearUpdateView.as_view(), name='campinggear_update'),
    path('campinggear/<int:pk>/delete/', CampingGearDeleteView.as_view(), name='campinggear_delete'),

    # Creator Gear
    path('creatorgear/', CreatorGearListView.as_view(), name='creatorgear_list'),
    path('creatorgear/<int:pk>/', CreatorGearDetailView.as_view(), name='creatorgear_detail'),
    path('creatorgear/add/', CreatorGearCreateView.as_view(), name='creatorgear_add'),
    path('creatorgear/<int:pk>/edit/', CreatorGearUpdateView.as_view(), name='creatorgear_update'),
    path('creatorgear/<int:pk>/delete/', CreatorGearDeleteView.as_view(), name='creatorgear_delete'),
]
