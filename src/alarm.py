from gpiozero import TonalBuzzer
from time import sleep
from time import time

def setOff(pin, duration):
    buzzer = TonalBuzzer(pin)
    buzzer.play("A4")
    startT = time() 
    while (time() - startT < duration):
        pass
    buzzer.stop()

def main():
    setOff(17, 8)

if __name__ == "__main__":
    main()
