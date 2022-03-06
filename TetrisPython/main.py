import RPi.GPIO as GPIO
import engine

GPIO.setmode(GPIO.BCM)

manager = engine.Manager(1)
display = engine.Display()

class GameState(engine.State):
    def initialize(self):
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

        # Wand zeichnen
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
        display.set_cursor(75, 2)
        display.draw([0xFF, 0x00, 0xFF]) # Untere Seite 4
        display.set_cursor_x(13)
        display.draw([0xFF, 0x00, 0xFF]) # Obere Seite 4
        display.set_cursor(75, 1)
        display.draw([0xFC, 0x01, 0xFE]) # Untere Seite 5
        display.set_cursor_x(13)
        display.draw([0xFF, 0x00, 0xFF]) # Obere Seite 5
        display.set_cursor(75, 0)
        display.draw([0x80, 0x00, 0x00]) # Untere Seite 6
        display.set_cursor_x(13)
        display.draw([0xFF, 0x00, 0xFF]) # Obere Seite 6

    def update(self, delta_time):
        pass

game_state = GameState()

display.initialize()

manager.set_state(game_state)
manager.start()

GPIO.cleanup()
