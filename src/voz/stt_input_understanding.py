import speech_recognition as sr
import logging


def stt_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text = r.listen(source)

        try:
            recognised_text = r.recognize_google(text, language="es-ESP")
        except sr.UnknownValueError:
            recognised_text = "UnknownValueError"
            logging.exception("error traceback")
        except sr.RequestError:
            recognised_text = "UnknownValueError"
            logging.exception("error traceback")
    return recognised_text

# if __name__ == "__main__":
#     STTInput()