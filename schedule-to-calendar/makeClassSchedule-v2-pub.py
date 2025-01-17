from datetime import datetime, timedelta

# This creates a calendar for your class schedule to import into google/apple/ms calendar

# Function to create repeating .ics events
def create_repeating_ics_event(name, location, start_time, end_time, days, start_date, end_date):
    """Generate a repeating .ics event for a class."""
    # Map days to weekdays (0 = Monday, ..., 6 = Sunday)
    day_mapping = {
        "Monday": "MO",
        "Tuesday": "TU",
        "Wednesday": "WE",
        "Thursday": "TH",
        "Friday": "FR",
        "Saturday": "SA",
        "Sunday": "SU",
    }
    rrule_days = ",".join([day_mapping[day] for day in days])
    start_datetime = datetime.strptime(f"{start_date.strftime('%Y%m%d')} {start_time}", "%Y%m%d %I:%M %p")
    end_datetime = datetime.strptime(f"{start_date.strftime('%Y%m%d')} {end_time}", "%Y%m%d %I:%M %p")
    
    event = f"""BEGIN:VEVENT
SUMMARY:{name}
LOCATION:{location}
DTSTART:{start_datetime.strftime('%Y%m%dT%H%M%S')}
DTEND:{end_datetime.strftime('%Y%m%dT%H%M%S')}
RRULE:FREQ=WEEKLY;BYDAY={rrule_days};UNTIL={end_date.strftime('%Y%m%dT235959')}
DESCRIPTION:Class Schedule
STATUS:CONFIRMED
SEQUENCE:0
END:VEVENT
"""
    return event


# Semester start and end dates - (YYYY, (M)M, (D)D)
semester_start = datetime(2025, 1, 27)
semester_end = datetime(2025, 5, 13)

# Class schedule details - CHANGE WITH YOUR OWN CLASSES AND DETAILS - see format examples
classes = [
    {
        "name": "CMPE 306 (LEC)",
        "start_time": "07:00 AM",
        "end_time": "07:50 AM",
        "days": ["Tuesday", "Thursday"],
        "location": "LH 1",
    },
    {
        "name": "CMPE 306 (LAB)",
        "start_time": "5:00 PM",
        "end_time": "6:50 PM",
        "days": ["Tuesday"],
        "location": "ECS 240",
    },
    {
        "name": "CMSC 341 (LEC)",
        "start_time": "2:00 PM",
        "end_time": "3:15 PM",
        "days": ["Tuesday", "Thursday"],
        "location": "LH 2",
    },
    {
        "name": "MATH 225 (LEC)",
        "start_time": "1:30 PM",
        "end_time": "2:45 PM",
        "days": ["Monday", "Wednesday"],
        "location": "MP 212",
    },
]

# Generate .ics content with repeating events and no alarms
ics_content = """BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
PRODID:-//My Class Schedule//DE
"""

for class_info in classes:
    # Find the first date that matches the first weekday in "days" for this class
    first_class_date = semester_start
    day_mapping = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}
    while first_class_date.weekday() not in [day_mapping[day] for day in class_info["days"]]:
        first_class_date += timedelta(days=1)

    ics_content += create_repeating_ics_event(
        name=class_info["name"],
        location=class_info["location"],
        start_time=class_info["start_time"],
        end_time=class_info["end_time"],
        days=class_info["days"],
        start_date=first_class_date,
        end_date=semester_end,
    )

ics_content += "END:VCALENDAR"

# Save the updated .ics file - REPLACE file_path WITH YOUR FILE PATH AND DESIRED CALENDAR NAME
file_path = "C:/Users/user123/Desktop/calendars/Spring25/spring25schedule.ics"  
with open(file_path, "w") as f:
    f.write(ics_content)

file_path

print("Done!")

# Chatgpt my goat