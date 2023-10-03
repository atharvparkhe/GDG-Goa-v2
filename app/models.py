from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


class PersonBaseModel(BaseModel):
    name = models.CharField(max_length=50)
    tagline = models.TextField()
    intro = models.TextField()
    img = models.ImageField(upload_to="team", height_field=None, width_field=None, max_length=None)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    x = models.URLField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        abstract = True


class EventTypeModel(BaseModel):
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category
    class Meta:
        db_table = 'event_type'
        verbose_name = "Event Type"

class VenueModel(BaseModel):
    name = models.CharField(max_length=70)
    address = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.venue
    class Meta:
        db_table = 'venue'
        verbose_name = "Venue"


class VenueImagesModel(BaseModel):
    venue = models.ForeignKey(VenueModel, related_name="venue_images", on_delete=models.CASCADE)
    img = models.ImageField(upload_to="venue", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.venue.name
    class Meta:
        db_table = 'venue_images'
        verbose_name = "Venue Image"


class SponsorsModel(BaseModel):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="sponsor", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'sponsors'
        verbose_name = "Sponsor"


class VolunteerModel(PersonBaseModel):
    class Meta:
        db_table = 'volunteer'
        verbose_name = "Volunteer"


class SpeakerModel(PersonBaseModel):
    class Meta:
        db_table = 'speaker'
        verbose_name = "Speaker"


class EventModel(BaseModel):
    name = models.CharField(max_length=100)
    intro = models.TextField()
    content = models.TextField()
    schedule = models.DateTimeField(auto_now=False, auto_now_add=False)
    venue = models.ForeignKey(VenueModel, related_name="event_venue", on_delete=models.PROTECT)
    template = models.CharField(max_length=50)
    team = models.ManyToManyField(VolunteerModel)
    sponsors = models.ManyToManyField(SponsorsModel)
    ticket = models.URLField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'event'
        verbose_name = "Event"


class EventScheduleModel(BaseModel):
    event = models.ForeignKey(EventModel, related_name="event_schedule_item", on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    speaker = models.ForeignKey(SpeakerModel, related_name="speakers_slot", on_delete=models.CASCADE)
    topic_info = models.TextField()
    def __str__(self):
        return self.event.name
    class Meta:
        db_table = 'schedule'
        verbose_name = "Schedule"
