from django.db import models

class Timetable(models.Model):
    name = models.CharField(max_length=100, default="My Timetable")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=10, help_text="e.g., PKP")

    def __str__(self):
        return f"{self.name} ({self.initials})"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, help_text="e.g., FSD-1")

    def __str__(self):
        return f"{self.name} ({self.code})"

class Room(models.Model):
    number = models.CharField(max_length=20, help_text="e.g., 410-C")

    def __str__(self):
        return self.number

class Division(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, related_name='divisions', null=True, blank=True)
    name = models.CharField(max_length=10, help_text="e.g., D1")

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, related_name='timeslots', null=True, blank=True)
    DAY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
    ]
    lecture_number = models.IntegerField(help_text="1, 2, 3...")
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_break = models.BooleanField(default=False)

    class Meta:
        ordering = ['lecture_number']

    def __str__(self):
        return f"Rec {self.lecture_number}: {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"

class TimetableEntry(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, related_name='entries', null=True, blank=True)
    day = models.CharField(max_length=3, choices=TimeSlot.DAY_CHOICES)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Timetable Entries"
        # Unique constraint needs to allow multiple timetables now. 
        # (timetable, day, timeslot, division) should be unique
    
    def __str__(self):
        return f"{self.day} - {self.timeslot} - {self.division}"
