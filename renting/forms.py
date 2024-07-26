# forms.py
from django import forms
from .models import TrekkingGear, Camera, RidingGear, ActionCamera, GamingConsole, WinterWear, AudioVisualEquipment, CampingGear, CreatorGear

class TrekkingGearForm(forms.ModelForm):
    class Meta:
        model = TrekkingGear
        fields = '__all__'

class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = '__all__'

class RidingGearForm(forms.ModelForm):
    class Meta:
        model = RidingGear
        fields = '__all__'

class ActionCameraForm(forms.ModelForm):
    class Meta:
        model = ActionCamera
        fields = '__all__'

class GamingConsoleForm(forms.ModelForm):
    class Meta:
        model = GamingConsole
        fields = '__all__'

class WinterWearForm(forms.ModelForm):
    class Meta:
        model = WinterWear
        fields = '__all__'

class AudioVisualEquipmentForm(forms.ModelForm):
    class Meta:
        model = AudioVisualEquipment
        fields = '__all__'

class CampingGearForm(forms.ModelForm):
    class Meta:
        model = CampingGear
        fields = '__all__'

class CreatorGearForm(forms.ModelForm):
    class Meta:
        model = CreatorGear
        fields = '__all__'
