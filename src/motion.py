from gpiozero import MotionSensor
from datetime import datetime
from time import sleep
from camera import capture

def trigger():
    timeStamp = datetime.now()
    fileName = "%04d-%02d-%02d-%02d-%02d-%02d.jpg" % (timeStamp.year, timeStamp.month, timeStamp.day, timeStamp.hour, timeStamp.minute, timeStamp.second)
    capture(fileName)
    print("saved %s" % fileName)

def main():
    pir = MotionSensor(4, queue_len=8)
    print("Monitoring motion. Interrupt process to stop...")
    while(True):
        pir.wait_for_motion()
        trigger()
        pir.wait_for_no_motion()
        sleep(2)

if __name__ == "__main__":
    main()
