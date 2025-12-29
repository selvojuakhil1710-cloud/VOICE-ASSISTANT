import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def get_audio():
    """Capture voice input"""
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"You said: {query}\n")
        return query.lower()

    except sr.WaitTimeoutError:
        print("Listening timed out")
        return ""

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""

    except sr.RequestError:
        speak("Network error. Please check your internet.")
        return ""

    except Exception as e:
        print(f"Error: {e}")
        return ""

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def tell_date():
    today = datetime.date.today()
    speak(f"Today's date is {today.strftime('%B %d, %Y')}")

def search_web(query):
    speak("Searching Google")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Main program
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = get_audio()

        if command == "":
            continue

        if "hello" in command:
            speak("Hello! How are you?")

        elif "your name" in command:
            speak("I am your beginner voice assistant.")

        elif "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "search for" in command:
            term = command.replace("search for", "").strip()
            search_web(term)

        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("Sorry, I can only do basic tasks like telling time, date, and searching.")
