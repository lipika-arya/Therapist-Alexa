import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
from textblob import TextBlob

recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()
voices = text_to_speech.getProperty('voices')
text_to_speech.setProperty('voice', voices[1].id)

def talk(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()

def listen_for_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        talk('Sorry, I couldn\'t understand. Can you please repeat?')
        return listen_for_command()
    except sr.RequestError as e:
        talk(f'Sorry, there was an error with the speech recognition service. Error: {e}')
        return None

    return command

def analyze_sentiment(command):
    blob = TextBlob(command)
    sentiment = blob.sentiment.polarity
    return sentiment

def run_assistant():
    command = listen_for_command()

    if command is not None:
        print(f"User said: {command}")
        sentiment = analyze_sentiment(command)

        # Decision logic based on sentiment
        if sentiment > 0:
            response = "That's great to hear!"
        elif sentiment < 0:
            response = "I'm sorry to hear that. How can I help?"
        else:
            response = "Neutral sentiment. Anything specific you'd like assistance with?"

        # Provide feedback to the user
        print(response)
        talk(response)

        # Process specific commands
        process_command(command)

def process_command(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'playing {song}')
        pywhatkit.playonyt(song)
    elif 'how are you' in command:
        talk('I am just a computer program, but I am here to help. How are you feeling today?')
    elif 'who is' in command:
        person = command.replace('who is', '')
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            talk(f"There are multiple results for {person}. Can you please specify?")
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    elif 'i need someone to talk to' in command:
        talk('I am here to listen. What is on your mind?')
    elif 'parents' in command:
        talk('Your parents love you the most. You are precious to them.')
    elif 'goodbye' in command:
        talk('Goodbye. Take care of yourself.')
        exit()  # Exit the program when the user says goodbye
    else:
        talk('Please share more about your feelings or ask a question.')

while True:
    run_assistant()
