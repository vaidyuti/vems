from django.contrib import admin

from .models import Generation, Load, Prosumer, Storage


class GenerationAdmin(admin.ModelAdmin):
    model = Generation


class LoadAdmin(admin.ModelAdmin):
    model = Load


class ProsumerAdmin(admin.ModelAdmin):
    model = Prosumer


class StorageAdmin(admin.ModelAdmin):
    model = Storage


admin.site.register(Generation, GenerationAdmin)
admin.site.register(Load, LoadAdmin)
admin.site.register(Prosumer, ProsumerAdmin)
admin.site.register(Storage, StorageAdmin)
