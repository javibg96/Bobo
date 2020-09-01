import src.interfaz.interfaz_handler as interfaz
import src.voz.stt_input_understanding as stt
import src.voz.tts_output as tts


class Cerebro:

    def __init__(self):
        self.voz = tts.Voz()

    def funciona(self):
        texto = stt.stt_input()
        while texto == "UnknownValueError":
            self.voz.habla("Disculpe señor, no he logrado entenderle, ¿Puede repetirmelo?")
            texto = stt.stt_input()

        print(texto)
        self.voz.habla("Encantado señor, ¿que quiere que haga?")
        texto2 = stt.stt_input()
        print(texto2)
        if "Spotify" in texto2:
            self.voz.habla("Iniciando Spotify...")


if __name__ == "__main__":
    Cerebro().funciona()
