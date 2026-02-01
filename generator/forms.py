from django import forms
from .models import TimetableEntry, TimeSlot, Division, Subject, Faculty, Room

class TimetableEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        timetable = kwargs.pop('timetable', None)
        super().__init__(*args, **kwargs)
        if timetable:
            self.fields['timeslot'].queryset = TimeSlot.objects.filter(timetable=timetable)
            self.fields['division'].queryset = Division.objects.filter(timetable=timetable)
        else:
            self.fields['timeslot'].queryset = TimeSlot.objects.none()
            self.fields['division'].queryset = Division.objects.none()

    class Meta:
        model = TimetableEntry
        fields = ['day', 'timeslot', 'division', 'subject', 'faculty', 'room']
        widgets = {
            'day': forms.Select(attrs={'class': 'form-control'}),
            'timeslot': forms.Select(attrs={'class': 'form-control'}),
            'division': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
        }

class SetupForm(forms.Form):
    divisions = forms.CharField(label="Divisions (Comma separated, e.g., D1, D2)", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'D1, D2, D3'}))
    start_time = forms.TimeField(label="First Lecture Start Time", widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'value': '08:45'}))
    slot_duration = forms.IntegerField(label="Lecture Duration (Minutes)", initial=60, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    break_duration = forms.IntegerField(label="Break Duration (Minutes)", initial=45, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # Simple configuration: How many slots before break?
    # Let's assume a pattern: x lectures, break, y lectures.
    slots_before_break = forms.IntegerField(label="Lectures before break", initial=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    slots_after_break = forms.IntegerField(label="Lectures after break", initial=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))

