from gpiozero import MotionSensor
from alarm import setOff

def trigger():
    # take a picture and send it to twilio or mitake
    # use setOff as a dummy function here
    print("motion detected")
    setOff(17, 1);

def main():
    pir = MotionSensor(4, queue_len=8)
    pir.when_motion = trigger;
    print("interrupt process to stop")
    while(True):
        pass

if __name__ == "__main__":
    main()
