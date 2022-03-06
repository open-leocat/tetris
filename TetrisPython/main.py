import RPi.GPIO as GPIO
import engine

GPIO.setmode(GPIO.BCM)

display = engine.Display()

display.clear()

# S
display.set_cursor(0, 5)
display.draw(0b00000000)
display.draw(0b00111100)
display.draw(0b01100000)
display.draw(0b00111100)
display.draw(0b00001110)
display.draw(0b01001110)
display.draw(0b00111100)

# C
display.set_cursor(0, 4)
display.draw(0b00000000)
display.draw(0b01111000)
display.draw(0b11001101)
display.draw(0b11000001)
display.draw(0b11000001)
display.draw(0b11001101)
display.draw(0b01111000)

# OR
display.set_cursor(0, 3)
display.draw(0b00000000)
display.draw(0b11110011)
display.draw(0b10011011)
display.draw(0b10011011)
display.draw(0b10011011)
display.draw(0b10011011)
display.draw(0b11110011)

# RE
display.set_cursor(0, 2)
display.draw(0b00000000)
display.draw(0b11100111)
display.draw(0b00110110)
display.draw(0b00110111)
display.draw(0b11100110)
display.draw(0b01000110)
display.draw(0b00110111)

GPIO.cleanup()
