import src.interfaz.interfaz_handler as interfaz
import src.interfaz.face_recon as f_r
import src.voz.stt_input_understanding as stt
import src.voz.tts_output as tts
import src.music_handler.music_handler as musica
import src.features.wikisearch as wiki
import json
import logging
import os


class Cerebro:
    def __init__(self):
        self.voz = tts.Voz()
        self.com_checker = False
        self.texto = " "
        FORMAT = '%(asctime)s--%(levelname)s--%(message)s'
        logging.basicConfig(format=FORMAT, level='INFO')
        self.logger = logging.getLogger("root")
        self.logger.setLevel(logging.INFO)
        face = True  # testing
        self.logger.info("Buenos dias")
        while not face:
            self.logger.info("Iniciando reconocimiento facial...")
            # face = f_r.recon()
            if face:
                self.voz.habla("Hola Javier, que tal esta")
            else:
                self.voz.habla("Disculpe señor, no le reconozco")

        with open("../src/comandos.json", "r", encoding='utf-8-sig') as raw_data:
            self.comandos = json.loads(raw_data.read())

    def funciona(self):
        self.logger.info("Inicio escucha")
        com_check = self.com_checker
        texto = " "
        while True:
            if not com_check:
                texto = stt.stt_input().lower()
                while texto == "unknownvalueerror":
                    self.voz.habla("¿Puede repetirmelo?")
                    texto = stt.stt_input().lower()
            else:
                while texto == " " or texto == "unknownvalueerror":
                    self.logger.info("Esperando entrada de voz o entrada no reconocida...")
                    texto = stt.stt_input().lower()
            print(texto)
            if texto == "youtube" and len(texto) == 7:
                texto = "youtube."
            self.texto = texto
            com_check = False

            for comando in self.comandos:
                if comando in texto:
                    com_check = True
                    texto = self.comando_handler(comando)

            if not com_check:
                self.voz.habla("Comando no reconocido")

    # funciones del asistente

    def espera(self):
        texto = stt.stt_input().lower()
        while texto == "UnknownValueError":
            self.voz.habla("Canción no reconocida, repitalo por favor")
            texto = stt.stt_input().lower()
        print(texto)
        m = musica.Musica()
        m.music(texto)
        texto = " "
        return texto

    def musica(self):
        m = musica.Musica()
        m.music(self.texto)
        texto = " "
        if " para" == texto:
            m.para()
        return texto

    def spoty(self):
        self.logger.info("Inicio spotify")
        os.system("spotify")
        texto = " "
        return texto

    def wiki(self):
        query = wiki.wikisearch(self.texto)
        self.voz.habla(query)
        texto = " "
        return texto

    def conv(self):
        self.logger.info("Inicio conversacion")
        texto = stt.stt_input().lower()
        while texto == "unknownvalueerror":
            self.voz.habla("No he entendido su respuesta, repita por favor")
            texto = stt.stt_input().lower()
        print(texto)
        if texto in self.comandos:
            respuesta = self.comandos[texto]["respuesta"]
            self.voz.habla(respuesta)  # por ahora max una conversacion de 2 respuestas
        return texto

    # funcion para manejar los comandos

    def comando_handler(self, comando):
        comando = self.comandos[comando]
        tipo = comando["tipo"]
        respuesta = comando["respuesta"]
        self.voz.habla(respuesta)

        # menu de comandos
        funciones = {
            "espera": self.espera,
            "musica": self.musica,
            "musica_spoti": self.spoty,
            "wikipedia": self.wiki,
            "conversación": self.conv
        }
        funcion = funciones.get(tipo, "comando no reconocido")
        texto = funcion()
        return texto


if __name__ == "__main__":
    Cerebro().funciona()
