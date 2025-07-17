import json
import dateparser
from datetime import datetime

reminders_file = "reminders.json"

def save_reminder(message, time_str):
    # Convert "tomorrow at 5" or "in 10 minutes" to actual date/time
    reminder_time = dateparser.parse(time_str)

    if reminder_time is None:
        print("Sorry, I couldn't understand the time you mentioned.")
        return

    if reminder_time <= datetime.now():
        print("The time you gave is already in the past.")
        return

    # Save to JSON file
    try:
        with open(reminders_file, 'r') as file:
            reminders = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        reminders = []

    reminders.append({
        "message": message,
        "time": reminder_time.strftime('%Y-%m-%d %H:%M:%S')
    })

    with open(reminders_file, 'w') as file:
        json.dump(reminders, file, indent=4)

    print(f"✅ Reminder saved for {reminder_time.strftime('%A, %I:%M %p')}")