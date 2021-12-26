from gpiozero import TonalBuzzer
from time import sleep

def setOff():
    n = 12
    buzzer = TonalBuzzer(17)
    for i in range(n):
        buzzer.play("A4")
        sleep(0.4)
        buzzer.stop()
        sleep(0.4)

def main():
    setOff()

if __name__ == "__main__":
    main()
