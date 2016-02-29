from django.contrib import admin

from events.models.concert import Concert
from events.models.excibition import Excibition
from events.models.meeting import Metting
from events.models.play import Play
from events.models.workshop import Workshop


class ConcertAdmin(admin.ModelAdmin):
    pass


class ExcibitionAdmin(admin.ModelAdmin):
    pass


class MettingAdmin(admin.ModelAdmin):
    pass


class PlayAdmin(admin.ModelAdmin):
    pass


class WorkshopAdmin(admin.ModelAdmin):
    pass


admin.site.register(Concert, ConcertAdmin)
admin.site.register(Excibition, ExcibitionAdmin)
admin.site.register(Metting, MettingAdmin)
admin.site.register(Play, PlayAdmin)
admin.site.register(Workshop, WorkshopAdmin)

