from django.contrib import admin
from .models import *


class VenueImagesModelAdmin(admin.StackedInline):
    model = VenueImagesModel
class VenueModelAdmin(admin.ModelAdmin):
    inlines = [VenueImagesModelAdmin]
    search_fields = ["name", "address"]
admin.site.register(VenueModel, VenueModelAdmin)


class SpeakerModelAdmin(admin.ModelAdmin):
    search_fields = ["name", "tagline"]
admin.site.register(SpeakerModel, SpeakerModelAdmin)


class VolunteerModelAdmin(admin.ModelAdmin):
    search_fields = ["name", "tagline"]
admin.site.register(VolunteerModel, VolunteerModelAdmin)


class SponsorsModelAdmin(admin.ModelAdmin):
    search_fields = ["name"]
admin.site.register(SponsorsModel, SponsorsModelAdmin)

