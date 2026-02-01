import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_project.settings')
django.setup()

from generator.models import Faculty, Subject, Room, Division, TimeSlot, TimetableEntry

def run():
    print("Cleaning old data...")
    TimetableEntry.objects.all().delete()
    TimeSlot.objects.all().delete()
    Division.objects.all().delete()
    Faculty.objects.all().delete()
    Subject.objects.all().delete()
    Room.objects.all().delete()

    print("Creating core data...")
    # Divisions
    divs = [Division.objects.create(name=f"D{i}") for i in range(1, 10)]
    
    # Faculties (Sample from image)
    faculties = {
        'SDP': Faculty.objects.create(name="Prof. Prashant Sachaniya", initials="SDP"),
        'MVK': Faculty.objects.create(name="Prof. Mehul Kodiya", initials="MVK"),
        'SHP': Faculty.objects.create(name="Prof. Swati Patel", initials="SHP"),
        'ZPB': Faculty.objects.create(name="Prof. Zalak Bhatt", initials="ZPB"),
        'PKP': Faculty.objects.create(name="Prof. Khushbu Patel", initials="PKP"),
        'PCS': Faculty.objects.create(name="Prof. Priyanka Sinha", initials="PCS"),
        'ZVB': Faculty.objects.create(name="Prof. Zarana Barot", initials="ZVB"),
        'DVB': Faculty.objects.create(name="Prof. Darshan Bhatt", initials="DVB"),
        'ZNP': Faculty.objects.create(name="Prof. Zalak Patel", initials="ZNP"),
    }

    # Subjects
    subjects = {
        'DE': Subject.objects.create(name="Digital Electronics", code="DE"),
        'FCSP-1': Subject.objects.create(name="Fundamentals of CS using Python", code="FCSP-1"),
        'FSD-1': Subject.objects.create(name="Full Stack Dev", code="FSD-1"),
        'PS': Subject.objects.create(name="Probability", code="PS"),
    }

    # Rooms
    rooms = {
        '208': Room.objects.create(number="208"),
        '410-C': Room.objects.create(number="410-C"),
        '306-5': Room.objects.create(number="306-5"),
        '306-4': Room.objects.create(number="306-4"),
        '306-6': Room.objects.create(number="306-6"),
        '203': Room.objects.create(number="203"),
        '309-B': Room.objects.create(number="309-B"),
        '204': Room.objects.create(number="204"),
        '205': Room.objects.create(number="205"),
    }

    # TimeSlots
    # Mon
    # 1: 8:45-9:45
    # 2: 9:45-10:45
    # Break: 10:45-11:30
    # 3: 11:30-12:30
    # 4: 12:30-1:30
    
    slots = []
    slots.append(TimeSlot.objects.create(lecture_number=1, start_time=datetime.time(8,45), end_time=datetime.time(9,45)))
    slots.append(TimeSlot.objects.create(lecture_number=2, start_time=datetime.time(9,45), end_time=datetime.time(10,45)))
    # Break is treated specially or just a slot? In my logic, it's a slot.
    # Note: Logic in template handles is_break.
    slots.append(TimeSlot.objects.create(lecture_number=0, start_time=datetime.time(10,45), end_time=datetime.time(11,30), is_break=True)) 
    # Use 0 or appropriate sorting. I'll use 2.5 conceptually but int required? 
    # Current model uses int. Let's start indices: 1, 2, 3 (break), 4, 5.
    
    # Cleaning slots:
    TimeSlot.objects.all().delete()
    
    ts1 = TimeSlot.objects.create(lecture_number=1, start_time=datetime.time(8,45), end_time=datetime.time(9,45))
    ts2 = TimeSlot.objects.create(lecture_number=2, start_time=datetime.time(9,45), end_time=datetime.time(10,45))
    ts_break = TimeSlot.objects.create(lecture_number=3, start_time=datetime.time(10,45), end_time=datetime.time(11,30), is_break=True)
    ts3 = TimeSlot.objects.create(lecture_number=4, start_time=datetime.time(11,30), end_time=datetime.time(12,30))
    ts4 = TimeSlot.objects.create(lecture_number=5, start_time=datetime.time(12,30), end_time=datetime.time(13,30))

    print("Creating Timetable Entries (Sample for Mon Slot 1)...")
    # Mon Slot 1
    # D1: DE, SDP, 208
    TimetableEntry.objects.create(day='MON', timeslot=ts1, division=divs[0], subject=subjects['DE'], faculty=faculties['SDP'], room=rooms['208'])
    # D2: FCSP-1, MVK, 410-C
    TimetableEntry.objects.create(day='MON', timeslot=ts1, division=divs[1], subject=subjects['FCSP-1'], faculty=faculties['MVK'], room=rooms['410-C'])
    # D3: FCSP-1, SHP, 306-5
    TimetableEntry.objects.create(day='MON', timeslot=ts1, division=divs[2], subject=subjects['FCSP-1'], faculty=faculties['SHP'], room=rooms['306-5'])

    # Slot 2 (Sample)
    # D1: DE, SDP, 208
    TimetableEntry.objects.create(day='MON', timeslot=ts2, division=divs[0], subject=subjects['DE'], faculty=faculties['SDP'], room=rooms['208'])

    print("Data seeded successfully!")

if __name__ == '__main__':
    run()
