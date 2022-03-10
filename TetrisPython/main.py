import engine
import RPi.GPIO as GPIO



manager = engine.Manager(8)

input = engine.Input()
display = engine.Display()



class GameState(engine.State):
    def initialize(self):
        ### Spielelogik vorbereiten

        # Ich denke, es ist erwähnenswert, dass ich keine Tetris-Konventionen einhalten werde. Aber das Projekt ist trotzdem an der Gameboy-Version inspiriert
        # Außerdem habe ich die Werte, wie zum Beispiel die Spielfeldgröße, "gehardcoded" statt diese variabel irgendwo zu definieren

        # Verschiedene Tetrominos initalisieren
        self.tetrominos = [[0, 0, 1, 0, # I
                            0, 0, 1, 0,
                            0, 0, 1, 0,
                            0, 0, 1, 0],
                           [0, 0, 1, 0, # Z
                            0, 1, 1, 0,
                            0, 1, 0, 0,
                            0, 0, 0, 0],
                           [0, 1, 0, 0, # S
                            0, 1, 1, 0,
                            0, 0, 1, 0,
                            0, 0, 0, 0],
                           [0, 0, 0, 0, # O
                            0, 1, 1, 0,
                            0, 1, 1, 0,
                            0, 0, 0, 0],
                           [0, 1, 1, 0, # J
                            0, 1, 0, 0,
                            0, 1, 0, 0,
                            0, 0, 0, 0],
                           [0, 1, 1, 0, # L
                            0, 0, 1, 0,
                            0, 0, 1, 0,
                            0, 0, 0, 0],
                           [0, 0, 1, 0, # T
                            0, 1, 1, 0,
                            0, 0, 1, 0,
                            0, 0, 0, 0]]

        # Spielefeld initalisieren (Breite=10, Höhe=17, Insgesamt=170)
        self.field = [0]*(170)

        # Jetzigen Tetromino initialisieren
        self.piece = 0
        self.piece_rotation = 0
        self.piece_x = 5
        self.piece_y = 0



        ### Grafik vorbereiten
        display.clear()

        # "SCORE"-Text zeichnen
        display.set_cursor(0, 5)
        display.draw([0x00, 0x3C, 0x60, 0x3C, 0x0E, 0x4E, 0x3C]) # S
        display.set_cursor(0, 4)
        display.draw([0x00, 0x78, 0xCD, 0xC1, 0xC1, 0xCD, 0x78]) # CO
        display.set_cursor(0, 3)
        display.draw([0x00, 0xF3, 0x9B, 0x9B, 0x9B, 0x9B, 0xF3]) # OR
        display.set_cursor(0, 2)
        display.draw([0x00, 0xE7, 0x36, 0x37, 0xE6, 0x46, 0x37]) # RE
        display.set_cursor(0, 1)
        display.draw([0x00, 0xE0, 0x00, 0xC0, 0x00, 0x00, 0xE0]) # E

        # Rahmen zeichnen
        display.set_cursor(13, 5)
        display.draw([0x01, 0x02, 0x04, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x04, 0x02, 0x01]) # Linke Seite

        display.set_cursor(75, 4)
        display.draw([0xFF, 0x00, 0xFF]) # Untere Seite 1
        display.set_cursor_x(13)
        display.draw([0xFF, 0x00, 0xFF]) # Obere Seite 1

        display.set_cursor(75, 3)
        display.draw([0xFF, 0x00, 0xFF]) # Untere Seite 2
        display.set_cursor_x(13)
        display.draw([0xFF, 0x00, 0xFF]) # Obere Seite 2

        display.set_cursor(75, 2)
        display.draw([0xFF, 0x00, 0xFF]) # Untere Seite 3
        display.set_cursor_x(13)
        display.draw([0xFF, 0x00, 0xFF]) # Obere Seite 3

        display.set_cursor(75, 1)
        display.draw([0xFC, 0x01, 0xFE]) # Untere Seite 4
        display.set_cursor_x(13)
        display.draw([0xFE, 0x01, 0xFC]) # Obere Seite 4

        display.set_cursor(75, 0)
        display.draw([0x80, 0x00, 0x00]) # Untere Seite 5
        display.set_cursor_x(13)
        display.draw([0x00, 0x00, 0x80]) # Obere Seite 5


    def update(self, delta_time):
        if input.is_pressed(0):
            # Links
            print("hello world")
            # if self.__tetromino_fit(self.piece, self.piece_rotation, self.piece_x - 1, self.piece_y):
            #     self.piece_x -= 1
            #
            #     # Den Tetromino zeichnen
            #
            #     px = int((3*self.piece_x + 5) / 6)
            #     py = self.piece_y * 3
            #
            #     display.set_cursor(60, px)
            #
            #     display.draw([0xFF])

    def __tetromino_rotate(self, x, y, rotation):
        temp = rotation % 4

        if temp == 0:
            return y * 4 + x
        elif temp == 1:
            return 12 + y - (x * 4)
        elif temp == 2:
            return 15 - (y * 4) - x
        elif temp == 3:
            return 3 - y + (x * 4)

        return 0

    def __tetromino_fit(self, id, x, y, rotation):
        return True

game_state = GameState()



GPIO.setmode(GPIO.BCM)

input.initialize()
display.initialize()

manager.set_state(game_state)
manager.start()
