import RPi.GPIO as GPIO
import engine

GPIO.setmode(GPIO.BCM)

display = engine.Display()

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



# import RPi.GPIO as GPIO
# import engine
#
# GPIO.setmode(GPIO.BCM)
#
# manager = engine.GameManager(2)
# display = engine.Display()
#
#
# # Der Zustand für das eigentliche Spiel
# class MainState(engine.GameState):
#     def initalize(self):
#         pass
#         # display.clear()
#
#         # "Score"-Text
#         # display.draw([0b11111111])
#         # display.set_cursor_y(5) # S
#         # display.draw([0x00, 0x3C, 0x60, 0x3C, 0x0E, 0x4E, 0x3C])
#         # display.set_cursor_y(4) # CO
#         # display.draw([0x00, 0x78, 0xCD, 0xC1, 0xC1, 0xCD, 0x78])
#         # display.set_cursor_y(3) # OR
#         # display.draw([0x00, 0xF3, 0x9B, 0x9B, 0x9B, 0x9B, 0xF3])
#         # display.set_cursor_y(2) # RE
#         # display.draw([0x00, 0xE7, 0x36, 0x37, 0xE6, 0x46, 0x37])
#         # display.set_cursor_y(1) # E
#         # display.draw([0x00, 0xE0, 0x00, 0xC0, 0x00, 0x00, 0xE0])
#         #
#
#     def update(self):
#         self.x = 0.0
#
#
#         if self.x >= 5.0:
#             manager.stop()
#
#         self.x += manager.delta
# main_state = MainState()
#
# manager.set_state(main_state)
# # manager.start()
# # manager.stop()
#
# display.clear()
# display.draw([0b11111111])
#
# GPIO.cleanup()
