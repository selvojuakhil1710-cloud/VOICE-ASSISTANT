import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def get_audio():
    """Capture voice input"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"You said: {query}\n")
    except Exception:
        speak("Sorry, I didn't catch that. Please say it again.")
        return ""
    
    return query.lower()

def tell_time():
    """Tell current time"""
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def tell_date():
    """Tell today's date"""
    today = datetime.date.today()
    speak(f"Today's date is {today.strftime('%B %d, %Y')}")

def search_web(query):
    """Search something on Google"""
    speak("Searching Google...")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Main program
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = get_audio()

        if "hello" in command:
            speak("Hello! How are you?")

        elif "your name" in command:
            speak("I am your beginner voice assistant.")

        elif "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "search for" in command:
            term = command.replace("search for", "")
            search_web(term)

        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye! Have a great day!")
            break

        elif command != "":
            speak("Sorry, I can only do basic tasks like telling time, date, and searching.")
