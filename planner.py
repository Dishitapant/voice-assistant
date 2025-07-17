from voice_output import speak
from voice_input import listen
import datetime

def handle_planner(command):
    if "set a reminder" in command:
        speak("What should I remind you?")
        reminder = listen()
        if reminder:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            with open("reminders.txt", "a") as f:
                f.write(f"[{time}] {reminder}\n")
            speak("Reminder added.")
    
    elif "what's on my schedule" in command or "reminders" in command:
        try:
            with open("reminders.txt", "r") as f:
                data = f.read()
                if data:
                    speak("Here's your schedule:")
                    print(data)
                else:
                    speak("No reminders found.")
        except FileNotFoundError:
            speak("You have no saved reminders yet.")