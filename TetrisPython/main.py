import RPi.GPIO as GPIO
import engine

GPIO.setmode(GPIO.BCM)

display = engine.Display()

# class GameState(engine.State):
#     def intialize(self):
#         pass
#
#     def update(self):
#         pass
# game_state = GameState()

display.clear()

# S
display.set_cursor(0, 5)
display.draw([0x00, 0x3C, 0x60, 0x3C, 0x0E, 0x4E, 0x3C])
# CO
display.set_cursor(0, 4)
display.draw([0x00, 0x78, 0xCD, 0xC1, 0xC1, 0xCD, 0x78])
# OR
display.set_cursor(0, 3)
display.draw([0x00, 0xF3, 0x9B, 0x9B, 0x9B, 0x9B, 0xF3])
# RE
display.set_cursor(0, 2)
display.draw([0x00, 0xE7, 0x36, 0x37, 0xE6, 0x46, 0x37])
# E
display.set_cursor(0, 1)
display.draw([0x00, 0xE0, 0x00, 0xC0, 0x00, 0x00, 0xE0])

GPIO.cleanup()
