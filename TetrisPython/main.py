import RPi.GPIO as GPIO
import engine

GPIO.setmode(GPIO.BCM)

manager = engine.GameManager(2)
display = engine.Display()

class MenuState(engine.GameState):
    def initalize():
        pass

    def update():
        pass
menu_state = MenuState()

class MainState(engine.GameState):
    def initalize():
        self.x = 0.0
        print("Initalized!")

    def update():
        if time > 5.0:
            printf("Finished!")
            manager.stop()

        print("Updated!")

        self.x += manager.delta
main_state = MainState()

class DefeatState(engine.GameState):
    def initalize():
        pass

    def update():
        pass
defeat_state = DefeatState()

manager.set_state(main_state)
manager.start()
manager.stop()

# display.clear()
#
# # S
# display.set_cursor_y(5)
# display.draw([0x00, 0x3C, 0x60, 0x3C, 0x0E, 0x4E, 0x3C])
# # CO
# display.set_cursor_y(4)
# display.draw([0x00, 0x78, 0xCD, 0xC1, 0xC1, 0xCD, 0x78])
# # OR
# display.set_cursor_y(3)
# display.draw([0x00, 0xF3, 0x9B, 0x9B, 0x9B, 0x9B, 0xF3])
# # RE
# display.set_cursor_y(2)
# display.draw([0x00, 0xE7, 0x36, 0x37, 0xE6, 0x46, 0x37])
# # E
# display.set_cursor_y(1)
# display.draw([0x00, 0xE0, 0x00, 0xC0, 0x00, 0x00, 0xE0])

GPIO.cleanup()
