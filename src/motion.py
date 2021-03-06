import os
from twilio.rest import Client
from imgurpython import ImgurClient
from gpiozero import MotionSensor
from datetime import datetime
from time import sleep
from picamera import PiCamera

twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_client = Client(twilio_account_sid, twilio_auth_token)
imgur_client_id = os.environ['IMGUR_CLIENT_ID']
imgur_client_secret = os.environ['IMGUR_CLIENT_SECRET']
imgur_client = ImgurClient(imgur_client_id, imgur_client_secret)


def trigger(camera):
    timeStamp = datetime.now()
    fileName = "%04d-%02d-%02d-%02d-%02d-%02d.jpg" % (timeStamp.year, timeStamp.month, timeStamp.day, timeStamp.hour, timeStamp.minute, timeStamp.second)
    camera.capture(fileName)
    print("saved %s" % fileName)
    image =  imgur_client.upload_from_path(fileName)
    print("uploaded %s, you can find it here: %s" % (fileName, image['link']))
    
    fromNumber = os.environ['SMS_FROM_NUMBER']
    toNumber = os.environ['SMS_TO_NUMBER']
    message = twilio_client.messages.create(
        body="Seems like this guy has entered your property. %s\nTo set off an alarm, send 'ALARM' to %s" % (image['link'], fromNumber),
#         media_url=[image['link']],
        from_=fromNumber,
        to=toNumber
    )
    print(message.sid)

def main():
    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview(alpha=200)
    pir = MotionSensor(4, queue_len=20, sample_rate=100, threshold=0.7)
    print("Monitoring motion. Interrupt process to stop...")
    while(True):
        pir.wait_for_motion()
        trigger(camera)
        pir.wait_for_no_motion()
        sleep(2)

if __name__ == "__main__":
    main()
