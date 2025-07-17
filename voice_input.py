import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command

    except sr.UnknownValueError:
        print("❗ Sorry, I didn’t catch that.")
        return None
    except sr.RequestError:
        print("❗ Speech service unavailable.")
        return None