import serial as serial
import time


class arduino:
    def __init__(self):
        self.ard = serial.Serial('COM3', 9600)
        time.sleep(1)

    def read_arduino(self):
        i = 0
        while i < 20:
            rawString = self.ard.readline()
            print(rawString.decode("ascii"))
            i += 1

        arduino.close()

    def write_arduino(self):

        self.ard.write(b'9')    # manda un 9 en binario al arduino
        self.ard.close()

