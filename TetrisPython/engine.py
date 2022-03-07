import time
import RPi.GPIO as GPIO



# https://www.sparkfun.com/datasheets/LCD/Monochrome/Nokia5110.pdf
class Display:
    def initialize(self):
        GPIO.setup(2, GPIO.OUT)  # GPIO 2  / RST
        GPIO.setup(3, GPIO.OUT)  # GPIO 3  / CE
        GPIO.setup(4, GPIO.OUT)  # GPIO 4  / DC
        GPIO.setup(17, GPIO.OUT) # GPIO 17 / DIN
        GPIO.setup(27, GPIO.OUT) # GPIO 27 / CLK

        # Setze das Display auf einen bekannten Zustand
        GPIO.output(2, 0)
        GPIO.output(2, 1)

        self.__command(0b00100001) # Signalisiert dem Display, dass erweiterte LCD-Befehle kommen, vertikaler Modus aus
        self.__command(0b10111111) # Setzt den Kontrast
        self.__command(0b00000100) # Setzt den Temperaturkoeffizient?
        self.__command(0b00010100) # Setzt den Bias Modus auf 1:48
        self.__command(0b00100000) # Signalisiert dem Display, dass einfache LCD-Befehle kommen
        self.__command(0b00001100) # Setzt das Display auf den normalen Modus

    def __send(self, command, data):
        # Befehl oder Daten?
        GPIO.output(4, command)
        GPIO.output(3, 0)

        # Sendet ein Byte bitweise und sendet jedes Mal einen Impuls an den Clock-Pin. (Theoretisch hätte man auch die SPI-Pins dafür verwenden können)
        i = 7
        while (i >= 0):
            GPIO.output(17, data & (1 << i))
            GPIO.output(27, 1)
            GPIO.output(27, 0)

            i -= 1

        GPIO.output(3, 1)

    def __command(self, data):
        self.__send(0, data)

    def __data(self, data):
        self.__send(1, data)

    def set_cursor_x(self, x):
        # Setze X RAM des Displays
        self.__command(0x80 | x)

    def set_cursor_y(self, y):
        # Setze Y RAM des Displays
        self.__command(0x40 | y)

    def set_cursor(self, x, y):
        self.__command(0x80 | x)
        self.__command(0x40 | y)

    def clear(self):
        self.set_cursor(0, 0)

        for i in range(4032):
            self.__data(0)

        self.set_cursor(0, 0)

    def draw(self, data):
        for b in data:
            self.__data(b)

    def __del__(self):
        pass

class State:
    def initialize(self):
        pass

    def update(self, delta_time):
        pass

class Manager:
    def __init__(self, tps):
        self.set_tps(tps)
        self.__running = False
        self.__state = State()

    def set_tps(self, tps):
        self.__tick_time = 1e9 / tps # Berechne Nanosekunden pro Tick

    def set_state(self, state):
        self.__state = state
        if self.__running:
            self.__state.initialize()

    def start(self):
        if self.__running:
            return
        self.__running = True

        self.__state.initialize()

        delta = 0.0
        last_time = time.time_ns()
        now_time = 0

        while self.__running:
            now_time = time.time_ns()
            delta += (now_time - last_time) / self.__tick_time # Berechne Deltazeit
            last_time = now_time

            if delta >= 1: # Wenn Tick vorbei -> Update und setze die Deltazeit zurück
                self.__state.update(delta)
                delta -= 1

    def stop(self):
        if not self.__running:
            return
        self.__running = False
