from picamera import PiCamera
from time import sleep
from datetime import datetime

def capture(fileName):
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture(fileName)
    camera.stop_preview()
    camera.close()

def main():
    timeStamp = datetime.now()
    fileName = "%04d-%02d-%02d-%02d-%02d-%02d.jpg" % (timeStamp.year, timeStamp.month, timeStamp.day, timeStamp.hour, timeStamp.minute, timeStamp.second)
    capture(fileName)
    print("saved %s" % fileName)

if __name__ == "__main__":
    main()
