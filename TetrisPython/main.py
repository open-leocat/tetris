import RPi.GPIO as GPIO
import engine

GPIO.setmode(GPIO.BCM)

manager = engine.GameManager(2)
display = engine.Display()

# Der Zustand für das Menü
class MenuState(engine.GameState):
    def initalize(self):
        pass

    def update(self):
        pass
menu_state = MenuState()

# Der Zustand für das eigentliche Spiel
class MainState(engine.GameState):
    def initalize(self):
        display.clear()

        # "Score"-Text
        display.set_cursor_y(5) # S
        display.draw([0x00, 0x3C, 0x60, 0x3C, 0x0E, 0x4E, 0x3C])
        display.set_cursor_y(4) # CO
        display.draw([0x00, 0x78, 0xCD, 0xC1, 0xC1, 0xCD, 0x78])
        display.set_cursor_y(3) # OR
        display.draw([0x00, 0xF3, 0x9B, 0x9B, 0x9B, 0x9B, 0xF3])
        display.set_cursor_y(2) # RE
        display.draw([0x00, 0xE7, 0x36, 0x37, 0xE6, 0x46, 0x37])
        display.set_cursor_y(1) # E
        display.draw([0x00, 0xE0, 0x00, 0xC0, 0x00, 0x00, 0xE0])

    def update(self):
        pass
main_state = MainState()

# Der Zustand für den GameOver Bildschirm
class DefeatState(engine.GameState):
    def initalize(self):
        pass

    def update(self):
        pass
defeat_state = DefeatState()

manager.set_state(main_state)
manager.start()
manager.stop()

GPIO.cleanup()
