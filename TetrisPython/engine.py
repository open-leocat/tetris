import RPi.GPIO as GPIO



class Display:
    def __init__(self):
        GPIO.setup(2, GPIO.OUT)  # GPIO 2  / RST
        GPIO.setup(3, GPIO.OUT)  # GPIO 3  / CE
        GPIO.setup(4, GPIO.OUT)  # GPIO 4  / DC
        GPIO.setup(17, GPIO.OUT) # GPIO 17 / DIN
        GPIO.setup(27, GPIO.OUT) # GPIO 27 / CLK

        GPIO.output(2, 0)
        GPIO.output(2, 1)

    def __command(self, command, data):
        GPIO.output(4, command)
        GPIO.output(3, 0)

        i = 7
        while (i >= 0):
            GPIO.output(17, data & (1 << i))
            GPIO.output(27, 1);
            GPIO.output(27, 0);

            i -= 1

        GPIO.output(3, 1)

    def clear(self):
        pass

    def draw(self, x, y, data):
        self.__command(0, 0b00100001 ); # LCD Extended Commands. You can use 0x21
        self.__command(0, 0b10110000 ); # Set LCD Vop (Contrast). You can use 0xB0
        self.__command(0, 0b00000100 ); # Set Temp coefficent. You can use 0x04
        self.__command(0, 0b00010100 ); # LCD bias mode 1:48. You can use 0x14
        self.__command(0, 0b00100000 ); # LCD Basic Commands. You can use 0x20
        self.__command(0, 0b00001100 ); # LCD in normal mode. You can use 0x0C
        self.__command(1, 0b00011111);
        self.__command(1, 0b00000101);
        self.__command(1, 0b00000111);
        self.__command(1, 0b00000000);
        self.__command(1, 0b00011111);
        self.__command(1, 0b00000100);
        self.__command(1, 0b00011111);
        self.__command(0, 0b00001101);
        self.__command(0, 0b10000000);
        self.__command(1, 0b00000000);

        pass

    def __del__(self):
        pass
