import RPi.GPIO as GPIO
import engine

GPIO.setmode(GPIO.BCM)

display = engine.Display()

display.clear()
display.set_cursor(40, 1)
display.draw(0b00111100)

GPIO.cleanup()
