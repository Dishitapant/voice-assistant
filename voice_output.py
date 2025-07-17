import pyttsx3

engine = pyttsx3.init()

# Optional: Customize voice and speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index for male/female voice
engine.setProperty('rate', 175)  # Speed of speech

def speak(text):
    print(f"🤖 Assistant: {text}")
    engine.say(text)
    engine.runAndWait()