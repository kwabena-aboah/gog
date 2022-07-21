from django.contrib import admin
from . models import Region, District, NationalReport


admin.site.register(Region)
admin.site.register(District)
admin.site.register(NationalReport)
# admin.site.register(PublicAuthority)