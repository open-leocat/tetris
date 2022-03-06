import RPi.GPIO as GPIO
import engine

GPIO.setmode(GPIO.BCM)

display = engine.Display()

display.clear()
display.set_cursor(0, 3)
display.draw(0b01111100)
display.draw(0b01111100)

GPIO.cleanup()
