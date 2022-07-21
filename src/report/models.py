from django.db import models
from . validators import validate_image_extension, validate_video_extension
from location_field.models.plain import PlainLocationField

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
    
    def __str__(self):
        return self.name
    


class District(models.Model):
    name = models.CharField(max_length=100, help_text='District or Municipal name')
    
    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'
    
    def __str__(self):
        return self.name
    


# class PublicAuthority(models.Model):
#     name = models.CharField(max_length=150, help_text='E.g Police force, etc')
#     contact = models.CharField(max_length=15)
    
#     class Meta:
#         verbose_name = 'Public Authority'
#         verbose_name_plural = 'Public Authorities'
    
#     def __str__(self):
#         return self.name
    

class NationalReport(models.Model):
    # region = models.ForeignKey(Region, on_delete=models.CASCADE)
    # district = models.ForeignKey(District, on_delete=models.CASCADE)
    public_authority = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(upload_to='pictures/%y-%m-%d/', validators=[validate_image_extension], null=True, blank=True)
    videos = models.FileField(upload_to='videos/%y-%m-%d/',validators=[validate_video_extension], null=True, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='National Report Title')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'National Report'
        verbose_name_plural = 'National Reports'
    
    def __str__(self):
        return self.title
    
    
    