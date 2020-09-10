import src.interfaz.interfaz_handler as interfaz
import src.interfaz.face_recon as f_r
import src.voz.stt_input_understanding as stt
import src.voz.tts_output as tts
import src.music_handler.music_handler as musica
import json
import logging
import os


class Cerebro:
    def __init__(self):
        self.voz = tts.Voz()
        self.com_checker = False
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

            com_check = False

            for comando in self.comandos:
                if comando in texto:
                    com_check = True
                    texto = self.comando_handler(texto, comando)

            if not com_check :
                self.voz.habla("Comando no reconocido")

    def comando_handler(self, texto, comando):
        comando = self.comandos[comando]
        tipo = comando["tipo"]
        respuesta = comando["respuesta"]
        self.voz.habla(respuesta)
        if texto == "youtube" and len(texto) == 7:
            texto = "youtube."
        if tipo == "espera":
            texto = stt.stt_input().lower()
            while texto == "UnknownValueError":
                self.voz.habla("Canción no reconocida, repitalo por favor")
                texto = stt.stt_input().lower()
            print(texto)
            m = musica.Musica()
            m.music(texto)
            texto = " "
        elif tipo == "musica":
            m = musica.Musica()
            m.music(texto)
            texto = " "
            if " para" == texto:
                m.para()
        elif tipo == "musica_spoti":
            self.logger.info("Inicio spotify")
            os.system("spotify")
            texto = " "
        elif tipo == "conversación":
            self.logger.info("Inicio conversacion")
            texto = stt.stt_input().lower()
            while texto == "unknownvalueerror":
                self.voz.habla("No he entendido su respuesta, repita por favor")
                texto = stt.stt_input().lower()
            print(texto)
            if texto in self.comandos:
                respuesta = self.comandos[texto]["respuesta"]
                self.voz.habla(respuesta)       # por ahora max una conversacion de 2 respuestas
        return texto


if __name__ == "__main__":
    Cerebro().funciona()
