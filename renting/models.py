from django.db import models

class TrekkingGear(models.Model):
    NAME_CHOICES = [
        ('binoculars', 'Binoculars'),
        ('trek_accessories', 'Trek Accessories'),
        ('trekking_shoes', 'Trekking Shoes'),
        ('trekking_jackets', 'Trekking Jackets'),
        ('trekking_backpacks', 'Trekking Backpacks'),
    ]
    
    name = models.CharField(max_length=50, choices=NAME_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='trekking_gear_images/')
    
    def __str__(self):
        return self.get_name_display()


#camera

class Camera(models.Model):
    CAMERA_TYPES = [
        ('dslr', 'DSLR'),
        ('mirrorless', 'Mirrorless'),
        ('compact', 'Compact'),
        ('binocular', 'Binocular'),
    ]
    
    name = models.CharField(max_length=100)
    camera_type = models.CharField(max_length=20, choices=CAMERA_TYPES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='camera_images/')
    
    def __str__(self):
        return self.name



class RidingGear(models.Model):
    RIDING_GEAR_CHOICES = [
        ('helmet', 'Helmet'),
        ('gloves', 'Gloves'),
        ('jacket', 'Jacket'),
        ('boots', 'Boots'),
    ]
    
    name = models.CharField(max_length=50, choices=RIDING_GEAR_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='riding_gear_images/')
    
    def __str__(self):
        return self.get_name_display()




class ActionCamera(models.Model):
    BRAND_CHOICES = [
        ('gopro', 'GoPro'),
        ('sjcam', 'SJCAM'),
        ('insta360', 'Insta360'),
        ('xiaomi', 'Xiaomi'),
    ]
    
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='action_camera_images/')
    
    def __str__(self):
        return self.name



class GamingConsole(models.Model):
    CONSOLE_CHOICES = [
        ('ps5', 'PlayStation 5'),
        ('xbox', 'Xbox Series X'),
        ('switch', 'Nintendo Switch'),
        ('pc', 'Gaming PC'),
    ]
    
    name = models.CharField(max_length=50, choices=CONSOLE_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='gaming_console_images/')
    
    def __str__(self):
        return self.get_name_display()
    


class WinterWear(models.Model):
    WINTER_WEAR_CHOICES = [
        ('jacket', 'Jacket'),
        ('gloves', 'Gloves'),
        ('hat', 'Hat'),
        ('scarf', 'Scarf'),
    ]
    
    name = models.CharField(max_length=50, choices=WINTER_WEAR_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='winter_wear_images/')
    
    def __str__(self):
        return self.get_name_display()




class AudioVisualEquipment(models.Model):
    EQUIPMENT_CHOICES = [
        ('projector', 'Projector'),
        ('microphone', 'Microphone'),
        ('speaker', 'Speaker'),
        ('vr', 'Vr'),
    ]
    
    name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=20, choices=EQUIPMENT_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='audio_visual_images/')
    
    def __str__(self):
        return self.name



class CampingGear(models.Model):
    CAMPING_GEAR_CHOICES = [
        ('tent', 'Tent'),
        ('sleeping_bag', 'Sleeping Bag'),
        ('stove', 'Stove'),
        ('backpack', 'Backpack'),
    ]
    
    name = models.CharField(max_length=50, choices=CAMPING_GEAR_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='camping_gear_images/')
    
    def __str__(self):
        return self.get_name_display()



from django.db import models

class CreatorGear(models.Model):
    CREATOR_GEAR_CHOICES = [
    ('action_cameras', 'Action Cameras'),
    ('wireless_mics', 'Wireless & Collar Mics'),
    ('professional_cameras', 'Professional Cameras'),
    ('vlogging_cameras', 'Vlogging Cameras'),
    ('mounts_accessories', 'Mounts & Accessories'),
    ('studio_lights', 'Studio Lights'),
    ('gimbals_grips', 'Gimbals and Grips'),
    
    ]

    
    name = models.CharField(max_length=50, choices=CREATOR_GEAR_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='creator_gear_images/')
    
    def __str__(self):
        return self.get_name_display()
