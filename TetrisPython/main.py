import RPi.GPIO as GPIO
import engine

GPIO.setmode(GPIO.BCM)

display = engine.Display()

display.clear()
display.draw(0b11111111)

GPIO.cleanup()
