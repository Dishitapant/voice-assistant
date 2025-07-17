from voice_input import listen
from voice_output import speak
import datetime
import webbrowser
import pyjokes
import os

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

def handle_command(command):
    command = command.lower()

    # Basic conversations
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you today?")
    elif "how are you" in command:
        speak("I'm just a program, but I'm happy to help!")
    elif "thank you" in command or "thanks" in command:
        speak("You're welcome!")
    elif "bye" in command or "goodbye" in command:
        speak("Goodbye! Have a nice day!")
        exit()

    # Utility commands
    elif "time" in command:
        speak(f"The time is {get_time()}")
    elif "date" in command:
        speak(f"Today's date is {get_date()}")
    elif "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://youtube.com")
    elif "tell me a joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif "weather" in command:
        speak("Here's the weather.")
        webbrowser.open("https://www.google.com/search?q=weather")
    elif "reminder" in command or "schedule" in command or "set a reminder" in command:
        from planner import handle_planner
        handle_planner(command)

    # Unknown command → Google Search fallback
    else:
        speak("I'm not sure, but here's what I found on Google.")
        query = command.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")

# Run assistant
while True:
    speak("I'm listening...")
    command = listen()
    if command:
        handle_command(command)