from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
from time import time

def setOff(pin, duration):
    buzzer = TonalBuzzer(pin)
    startT = time() 
    for i in range(duration):
        buzzer.play(Tone(640.0))
        sleep(0.5)
        buzzer.play(Tone(853.0))
        sleep(0.5)
    buzzer.stop()

def main():
    setOff(17, 8)

if __name__ == "__main__":
    main()
