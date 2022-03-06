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

# # OR
# display.set_cursor(0, 3)
# display.draw(0b00000000)
# display.draw(0b11110011)
# display.draw(0b10011011)
# display.draw(0b10011011)
# display.draw(0b10011011)
# display.draw(0b10011011)
# display.draw(0b11110011)
#
# # RE
# display.set_cursor(0, 2)
# display.draw(0b00000000)
# display.draw(0b11100111)
# display.draw(0b00110110)
# display.draw(0b00110111)
# display.draw(0b11100110)
# display.draw(0b01000110)
# display.draw(0b00110111)
#
# # E
# display.set_cursor(0, 1)
# display.draw(0b00000000)
# display.draw(0b11100000)
# display.draw(0b00000000)
# display.draw(0b11000000)
# display.draw(0b00000000)
# display.draw(0b00000000)
# display.draw(0b11100000)

GPIO.cleanup()
