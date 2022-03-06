import RPi.GPIO as GPIO
import engine

GPIO.setmode(GPIO.BCM)

display = engine.Display()

display.clear()
display.set_cursor(0, 5)
display.draw(0b00000000)
display.draw(0b00111100)
display.draw(0b01100000)
display.draw(0b00111100)
display.draw(0b00001110)
display.draw(0b01001110)
display.draw(0b00111100)

GPIO.cleanup()
