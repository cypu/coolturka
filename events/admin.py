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


admin.register.site(Concert, ConcertAdmin)
admin.register.site(Excibition, ExcibitionAdmin)
admin.register.site(Metting, MettingAdmin)
admin.register.site(Play, PlayAdmin)
admin.register.site(Workshop, WorkshopAdmin)

