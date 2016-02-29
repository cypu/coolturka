from django.contrib import admin
from locations.models.city import City
from locations.models.voivodeship import Voivodeship


class CityAdmin(admin.ModelAdmin):
    pass


class VoivodeshipAdmin(admin.ModelAdmin):
    pass


admin.site.register(City, CityAdmin)
admin.site.register(Voivodeship, VoivodeshipAdmin)
