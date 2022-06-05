import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 165)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    text = input("Enter Text you wish to be spoken")
    speak(text)