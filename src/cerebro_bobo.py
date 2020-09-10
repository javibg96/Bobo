import src.interfaz.interfaz_handler as interfaz
import src.interfaz.face_recon as f_r
import src.voz.stt_input_understanding as stt
import src.voz.tts_output as tts
import src.music_handler.spoty_handler as spoty
import json
import logging


class Cerebro:

    def __init__(self):
        self.voz = tts.Voz()
        face = True  # testing
        logging.warning("Buenos dias")
        while not face:
            logging.info("Iniciando reconocimiento facial...")
            # face = f_r.recon()
            if face:
                self.voz.habla("Hola Javier, que tal esta")
            else:
                self.voz.habla("Disculpe señor, no le reconozco")

        with open("../src/comandos.json", "r", encoding='utf-8-sig') as raw_data:
            self.comandos = json.loads(raw_data.read())

    def funciona(self):
        logging.warning("Inicio escucha")
        while True:
            texto = stt.stt_input()
            while texto == "UnknownValueError":
                self.voz.habla("¿Puede repetirmelo?")
                texto = stt.stt_input()
            print(texto)

            self.voz.habla("¿que quiere que haga?")
            texto2 = stt.stt_input()
            print(texto2)
            while texto2 == "UnknownValueError":
                texto2 = stt.stt_input()
                print(texto2)
                self.voz.habla("No he logrado entenderle")

            comando_checker = False

            for comando in self.comandos:
                if comando in texto2:
                    comando_checker = True
                    self.comando_handler(texto2, comando)

            if not comando_checker:
                self.voz.habla("Comando no reconocido")

    def comando_handler(self, texto, comando):
        comando = self.comandos[comando]
        tipo = comando["tipo"]
        respuesta = comando["respuesta"]
        self.voz.habla(respuesta)
        if tipo == "espera":
            texto = stt.stt_input()
            while texto == "UnknownValueError":
                self.voz.habla("Canción no reconocida, repitalo por favor")
                texto = stt.stt_input()
            print(texto)
            m = spoty.Musica()
            m.music(texto)
        if tipo == "musica":
            m = spoty.Musica()
            m.music(texto)
            if " para" == texto:
                m.para()


if __name__ == "__main__":
    Cerebro().funciona()
