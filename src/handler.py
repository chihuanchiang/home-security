from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from alarm import setOff

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    body = request.values.get('Body', None)
    resp = MessagingResponse()

    if body == 'ALARM':
        setOff(17,8)
        resp.message("Alarm set off")
    else:
        resp.message("Nothing happened")

    return str(resp)

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
