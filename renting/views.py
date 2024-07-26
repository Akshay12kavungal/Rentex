from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TrekkingGear, Camera, RidingGear, ActionCamera, GamingConsole, WinterWear, AudioVisualEquipment, CampingGear, CreatorGear
from .forms import TrekkingGearForm, CameraForm, RidingGearForm, ActionCameraForm, GamingConsoleForm, WinterWearForm, AudioVisualEquipmentForm, CampingGearForm, CreatorGearForm
from django.contrib.auth.decorators import login_required


def home(request):
    # Fetching one example item from each category
    example_camera = Camera.objects.first()
    example_trekking_gear = TrekkingGear.objects.first()
    example_riding_gear = RidingGear.objects.first()

    context = {
        'example_camera': example_camera,
        'example_trekking_gear': example_trekking_gear,
        'example_riding_gear': example_riding_gear,
    }
    return render(request, 'home.html', context)


# Trekking Gear views
class TrekkingGearListView(ListView):
    model = TrekkingGear
    template_name = 'trekking/list.html'

class TrekkingGearDetailView(DetailView):
    model = TrekkingGear
    template_name = 'trekking/detail.html'

class TrekkingGearCreateView(CreateView):
    model = TrekkingGear
    form_class = TrekkingGearForm
    template_name = 'trekking/form.html'
    success_url = reverse_lazy('trekkinggear_list')

class TrekkingGearUpdateView(UpdateView):
    model = TrekkingGear
    form_class = TrekkingGearForm
    template_name = 'trekking/update_form.html'
    success_url = reverse_lazy('trekkinggear_list')

class TrekkingGearDeleteView(DeleteView):
    model = TrekkingGear
    template_name = 'trekking/confirm_delete.html'
    success_url = reverse_lazy('trekkinggear_list')

# Camera views
class CameraListView(ListView):
    model = Camera
    template_name = 'camera/list.html'

class CameraDetailView(DetailView):
    model = Camera
    template_name = 'camera/detail.html'

class CameraCreateView(CreateView):
    model = Camera
    form_class = CameraForm
    template_name = 'camera/form.html'
    success_url = reverse_lazy('camera_list')

class CameraUpdateView(UpdateView):
    model = Camera
    form_class = CameraForm
    template_name = 'camera/update_form.html'
    success_url = reverse_lazy('camera_list')

class CameraDeleteView(DeleteView):
    model = Camera
    template_name = 'camera/confirm_delete.html'
    success_url = reverse_lazy('camera_list')

# Riding Gear views
class RidingGearListView(ListView):
    model = RidingGear
    template_name = 'ridinggear/list.html'

class RidingGearDetailView(DetailView):
    model = RidingGear
    template_name = 'ridinggear/detail.html'

class RidingGearCreateView(CreateView):
    model = RidingGear
    form_class = RidingGearForm
    template_name = 'ridinggear/form.html'
    success_url = reverse_lazy('ridinggear_list')

class RidingGearUpdateView(UpdateView):
    model = RidingGear
    form_class = RidingGearForm
    template_name = 'ridinggear/update_form.html'
    success_url = reverse_lazy('ridinggear_list')

class RidingGearDeleteView(DeleteView):
    model = RidingGear
    template_name = 'ridinggear/confirm_delete.html'
    success_url = reverse_lazy('ridinggear_list')

# Action Camera views
class ActionCameraListView(ListView):
    model = ActionCamera
    template_name = 'actioncamera/list.html'

class ActionCameraDetailView(DetailView):
    model = ActionCamera
    template_name = 'actioncamera/detail.html'

class ActionCameraCreateView(CreateView):
    model = ActionCamera
    form_class = ActionCameraForm
    template_name = 'actioncamera/form.html'
    success_url = reverse_lazy('actioncamera_list')

class ActionCameraUpdateView(UpdateView):
    model = ActionCamera
    form_class = ActionCameraForm
    template_name = 'actioncamera/update_form.html'
    success_url = reverse_lazy('actioncamera_list')

class ActionCameraDeleteView(DeleteView):
    model = ActionCamera
    template_name = 'actioncamera/confirm_delete.html'
    success_url = reverse_lazy('actioncamera_list')

# Gaming Console views
class GamingConsoleListView(ListView):
    model = GamingConsole
    template_name = 'gamingconsole/list.html'

class GamingConsoleDetailView(DetailView):
    model = GamingConsole
    template_name = 'gamingconsole/detail.html'

class GamingConsoleCreateView(CreateView):
    model = GamingConsole
    form_class = GamingConsoleForm
    template_name = 'gamingconsole/form.html'
    success_url = reverse_lazy('gamingconsole_list')

class GamingConsoleUpdateView(UpdateView):
    model = GamingConsole
    form_class = GamingConsoleForm
    template_name = 'gamingconsole/update_form.html'
    success_url = reverse_lazy('gamingconsole_list')

class GamingConsoleDeleteView(DeleteView):
    model = GamingConsole
    template_name = 'gamingconsole/confirm_delete.html'
    success_url = reverse_lazy('gamingconsole_list')

# Winter Wear views
class WinterWearListView(ListView):
    model = WinterWear
    template_name = 'winterwear/list.html'

class WinterWearDetailView(DetailView):
    model = WinterWear
    template_name = 'winterwear/detail.html'

class WinterWearCreateView(CreateView):
    model = WinterWear
    form_class = WinterWearForm
    template_name = 'winterwear/form.html'
    success_url = reverse_lazy('winterwear_list')

class WinterWearUpdateView(UpdateView):
    model = WinterWear
    form_class = WinterWearForm
    template_name = 'winterwear/update_form.html'
    success_url = reverse_lazy('winterwear_list')

class WinterWearDeleteView(DeleteView):
    model = WinterWear
    template_name = 'winterwear/confirm_delete.html'
    success_url = reverse_lazy('winterwear_list')

# Audio Visual Equipment views
class AudioVisualEquipmentListView(ListView):
    model = AudioVisualEquipment
    template_name = 'audiovisualequipment/list.html'

class AudioVisualEquipmentDetailView(DetailView):
    model = AudioVisualEquipment
    template_name = 'audiovisualequipment/detail.html'

class AudioVisualEquipmentCreateView(CreateView):
    model = AudioVisualEquipment
    form_class = AudioVisualEquipmentForm
    template_name = 'audiovisualequipment/form.html'
    success_url = reverse_lazy('audiovisual_list')

class AudioVisualEquipmentUpdateView(UpdateView):
    model = AudioVisualEquipment
    form_class = AudioVisualEquipmentForm
    template_name = 'audiovisualequipment/update_form.html'
    success_url = reverse_lazy('audiovisual_list')

class AudioVisualEquipmentDeleteView(DeleteView):
    model = AudioVisualEquipment
    template_name = 'audiovisualequipment/confirm_delete.html'
    success_url = reverse_lazy('audiovisual_list')

# Camping Gear views
class CampingGearListView(ListView):
    model = CampingGear
    template_name = 'campinggear/list.html'

class CampingGearDetailView(DetailView):
    model = CampingGear
    template_name = 'campinggear/detail.html'

class CampingGearCreateView(CreateView):
    model = CampingGear
    form_class = CampingGearForm
    template_name = 'campinggear/form.html'
    success_url = reverse_lazy('campinggear_list')

class CampingGearUpdateView(UpdateView):
    model = CampingGear
    form_class = CampingGearForm
    template_name = 'campinggear/update_form.html'
    success_url = reverse_lazy('campinggear_list')

class CampingGearDeleteView(DeleteView):
    model = CampingGear
    template_name = 'campinggear/confirm_delete.html'
    success_url = reverse_lazy('campinggear_list')

# Creator Gear views
class CreatorGearListView(ListView):
    model = CreatorGear
    template_name = 'creatorgear/list.html'

class CreatorGearDetailView(DetailView):
    model = CreatorGear
    template_name = 'creatorgear/detail.html'

class CreatorGearCreateView(CreateView):
    model = CreatorGear
    form_class = CreatorGearForm
    template_name = 'creatorgear/form.html'
    success_url = reverse_lazy('creatorgear_list')

class CreatorGearUpdateView(UpdateView):
    model = CreatorGear
    form_class = CreatorGearForm
    template_name = 'creatorgear/update_form.html'
    success_url = reverse_lazy('creatorgear_list')

class CreatorGearDeleteView(DeleteView):
    model = CreatorGear
    template_name = 'creatorgear/confirm_delete.html'
    success_url = reverse_lazy('creatorgear_list')
