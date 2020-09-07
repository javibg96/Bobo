import src.interfaz.interfaz_handler as interfaz
import src.interfaz.face_recon as f_r
import src.voz.stt_input_understanding as stt
import src.voz.tts_output as tts
import src.music_handler.spoty_handler as spoty


class Cerebro:

    def __init__(self):
        self.voz = tts.Voz()

    def funciona(self):
        face = f_r.recon()
        if face:
            self.voz.habla("Hola Javier, que tal esta")
        else:
            self.voz.habla("Disculpe señor, no le reconozco")
        texto = stt.stt_input()
        while texto == "UnknownValueError":
            self.voz.habla("Disculpe señor, no he logrado entenderle, ¿Puede repetirmelo?")
            texto = stt.stt_input()

        print(texto)
        self.voz.habla("Encantado señor, ¿que quiere que haga?")
        texto2 = stt.stt_input()
        print(texto2)
        m = spoty.Musica()
        if "Spotify" or "música" in texto2:
            self.voz.habla("Iniciando música...")
            busqueda = texto2.replace("musica", "").replace("Spotify", "").replace(" en ", "").replace(" in ",
                                                                                                       "").replace(
                " and ", "").replace(" ", "+").replace("Youtube", "")
            print(busqueda)
            m.music(busqueda)
        texto3 = stt.stt_input()
        comandos = ["wikipedia", "maps"]

        while texto3 == "UnknownValueError":
            texto3 = stt.stt_input()
            print(texto3)

            if "para" == texto3:
                m.para()

            elif texto3 != "UnknownValueError":
                self.voz.habla("me quedo a la espera de nuevas ordenes, señor")

            for comando in comandos:
                if comando not in texto3:
                    if "para" != texto3:
                        self.voz.habla("Comando no reconocido")
                    texto3 = "UnknownValueError"


if __name__ == "__main__":
    Cerebro().funciona()
