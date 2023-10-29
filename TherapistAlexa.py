import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

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
    except:
        pass
    return command

def run_assistant():
    command = listen_for_command()
    print(command)
    
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'how are you' in command:
        talk('I am just a computer program, but I am here to help. How are you feeling today?')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    elif 'i need someone to talk to' in command:
        talk('I am here to listen. What is on your mind?')
    elif 'parents' in command:
        talk('Your parents loves you the most. You are precious to them.')    
    elif 'goodbye' in command:
        talk('Goodbye. Take care of yourself.')
        exit()  # Exit the program when the user says goodbye
    else:
        talk('Please share more about your feelings or ask a question.')
    

while True:
    run_assistant()
