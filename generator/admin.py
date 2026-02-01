from django.contrib import admin
from .models import Faculty, Subject, Room, Division, TimeSlot, TimetableEntry

admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Room)
admin.site.register(Division)
admin.site.register(TimeSlot)

@admin.register(TimetableEntry)
class TimetableEntryAdmin(admin.ModelAdmin):
    list_display = ('day', 'timeslot', 'division', 'subject', 'faculty', 'room')
    list_filter = ('day', 'division', 'faculty', 'room')
