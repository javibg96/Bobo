import pyttsx3 as p


class Voz:
    def __init__(self):
        self.engine = p.init()
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[2].id)
        rate = self.engine.getProperty('rate')  # getting details of current speaking rate
        self.engine.setProperty('rate', 150)  # setting up new voice rate
        self.engine.runAndWait()

    def habla(self, frase):
        self.engine.say(frase)
        self.engine.runAndWait()
